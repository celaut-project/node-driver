import socket
from time import sleep
from datetime import datetime, timedelta
from threading import Thread, Lock

from utils.lambdas import LOGGER, SHA3_256_ID, STATIC_SERVICE_DIRECTORY, DYNAMIC_SERVICE_DIRECTORY, SHA3_256
from utils.network import is_open
from utils.read_file import read_file
from utils.singleton import Singleton
from utils.get_grpc_uri import get_grpc_uri

from protos import celaut_pb2 as celaut

from gateway.communication import generate_gateway_stub, stop, launch_instance, generate_instance_stub
from gateway.protos import gateway_pb2

# Si se toma una instancia, se debe de asegurar que, o bien se agrega a su cola
#  correspondiente, o bien se para. No asegurar esto ocasiona un bug importante
#  ya que las instancias quedarían zombies en la red hasta que el servicio
#  fuera eliminado.

class ServiceInstance(object):
    def __init__(self, stub, token, check_if_is_alive):
        self.stub = stub
        self.token = token
        self.creation_datetime = datetime.now()
        self.use_datetime = datetime.now()
        self.pass_timeout = 0
        self.failed_attempts = 0
        self.check_if_is_alive = check_if_is_alive

    def error(self):
        sleep(1) # Wait if the service is loading.
        self.failed_attempts = self.failed_attempts + 1

    def is_zombie(self,
                  pass_timeout_times,
                  timeout,
                  failed_attempts
                  ) -> bool:
        # In case it takes a long time to respond,
        #  check that the instance is still working
        return self.pass_timeout > pass_timeout_times and \
               not self.check_if_is_alive(timeout=timeout) \
               or self.failed_attempts > failed_attempts

    def timeout_passed(self):
        self.pass_timeout = self.pass_timeout + 1

    def reset_timers(self):
        self.pass_timeout = 0
        self.failed_attempts = 0

    def mark_time(self):
        self.use_datetime = datetime.now()

    def stop(self, gateway_stub):
        stop(gateway_stub=gateway_stub, token=self.token)

class ServiceConfig(object):
    def __init__(self,
                 service_with_config: gateway_pb2.ServiceWithConfig,
                 service_hash: str, stub_class,
                 check_if_is_alive = None,
                 timeout = 30,
                 failed_attempts = 5,
                 pass_timeout_times = 5
            ):

        self.stub_class = stub_class

        self.service_hash = service_hash  # SHA3-256 hash value that identifies the service definition on memory (if it's not complete is the hash of the incomplete definition).
        try:
            self.hashes = service_with_config.meta.hashtag.hash # list of hashes that the service's metadata has.
        except:  # if there are no hashes in the metadata
            if service_with_config.meta.complete: # if the service definition say that it's complete, the service hash can be used.
                self.hashes = [celaut.Any.HashTag.hash(
                    type = SHA3_256_ID,
                    value = bytes.fromhex(service_hash)
                )]
            else:
                self.hashes = []

        # Service configuration.
        self.config = celaut.Configuration()
        self.config.enviroment_variables.update(service_with_config.enviroment_variables)

        # Service's instances.
        self.instances = []  # se da uso de una pila para que el 'maintainer' detecte las instancias que quedan en desuso,
        #  ya que quedarán estancadas al final de la pila.

        self.check_if_is_alive = check_if_is_alive
        self.timeout = timeout,
        self.failed_attempts = failed_attempts,
        self.pass_timeout_times = pass_timeout_times

    def add_instance(self, instance: ServiceInstance, deep=False):
        LOGGER('Add instance ' + str(instance))
        self.instances.append(instance) if not deep else self.instances.insert(0, instance)

    def get_instance(self, deep=False) -> ServiceInstance:
        LOGGER('Get an instance of. deep ' + str(deep))
        LOGGER('The service ' + self.hashes[0].value.hex() + ' has ' + str(len(self.instances)) + ' instances.')
        try:
            return self.instances.pop() if not deep else self.instances.pop(0)
        except IndexError:
            LOGGER('    list empty --> ' + str(self.instances))
            raise IndexError
    
    def get_service_with_config(self) -> gateway_pb2.ServiceWithConfig:
        service_with_meta = gateway_pb2.ServiceWithMeta()
        service_with_meta.ParseFromString(
            read_file(DYNAMIC_SERVICE_DIRECTORY + self.service_hash + '/p1')
        )
        service_with_meta.ParseFromString(
            read_file(DYNAMIC_SERVICE_DIRECTORY + self.service_hash + '/p2')
        )
        return gateway_pb2.ServiceWithConfig(
                    meta = service_with_meta.meta,
                    definition = service_with_meta.service,
                    config = self.config
                )

    def launch_instance(self, gateway_stub) -> ServiceInstance:
        instance = launch_instance(
            gateway_stub = gateway_stub,
            service_hash = self.service_hash,
            hashes = self.hashes,
            config = self.config,
            static_service_directory = STATIC_SERVICE_DIRECTORY,
            dynamic_service_directory = DYNAMIC_SERVICE_DIRECTORY
        )

        try:
            uri = get_grpc_uri(instance.instance)
        except Exception as e:
            LOGGER(str(e))
            raise e
        LOGGER('The uri for the service ' + self.service_hash + ' is--> ' + str(uri))

        return ServiceInstance(
            stub=generate_instance_stub(self.stub_class, uri),
            token=instance.token,
            check_if_is_alive=self.check_if_is_alive if self.check_if_is_alive \
                else lambda timeout: is_open(timeout=timeout, ip=uri.ip, port=uri.port)
        )


MAINTENANCE_SLEEP_TIME_DEFAULT = 60
TIMEOUT_DEFAULT = 30
FAILED_ATTEMPTS_DEFAULT = 5
PASS_TIMEOUT_TIMES_DEFAULT = 5

class DependencyManager(metaclass = Singleton):

    def __init__(self,
                 gateway_main_dir: str,
                 maintenance_sleep_time: int = MAINTENANCE_SLEEP_TIME_DEFAULT,
                 timeout: int = TIMEOUT_DEFAULT,
                 failed_attempts: int = FAILED_ATTEMPTS_DEFAULT,
                 pass_timeout_times: int = PASS_TIMEOUT_TIMES_DEFAULT
            ):

        self.maintenance_sleep_time = maintenance_sleep_time
        self.timeout = timeout
        self.failed_attempts = failed_attempts
        self.pass_timeout_times = pass_timeout_times


        self.services = {}
        self.gateway_stub = generate_gateway_stub(gateway_main_dir)
        self.lock = Lock()
        Thread(target=self.maintenance, name='DepedencyMaintainer').start()


    def maintenance(self):
        while True:
            sleep(self.maintenance_sleep_time)
            index = 0
            while True:  # Si hacemos for service in services habría que bloquear el bucle entero.
                LOGGER('maintainer want services lock' + str(self.lock.locked()))
                self.lock.acquire()

                try:
                    service_config = self.services[
                        list(self.services)[index]
                    ]
                    index += 1
                    try:
                        instance = service_config.get_instance(deep=True)

                    except IndexError:
                        # No hay instancias disponibles en esta cola.
                        self.lock.release()
                        continue
                except IndexError:
                    LOGGER('All services have been toured.')
                    self.lock.release()
                    break
                except Exception as e:
                    LOGGER('ERROR on maintainer, ' + str(e))
                    self.lock.release()
                    break
                self.lock.release()

                LOGGER('      maintain service instance --> ' + str(instance))
                # En caso de que lleve mas de demasiado tiempo sin usarse.
                # o se encuentre en estado 'zombie'
                if datetime.now() - instance.use_datetime > timedelta(
                        minutes = self.maintenance_sleep_time) \
                        or instance.is_zombie(
                    pass_timeout_times = service_config.pass_timeout_times,
                    timeout = service_config.timeout,
                    failed_attempts = service_config.failed_attempts
                ):
                    instance.stop(self.gateway_stub)
                # En caso contrario añade de nuevo la instancia a su respectiva cola.
                else:
                    self.lock.acquire()
                    service_config.add_instance(instance, deep = True)
                    self.lock.release()

    def add_service(self,
                    service_with_config: gateway_pb2.ServiceWithConfig,
                    service_config_id: str,
                    service_hash: str,
                    stub_class,
                    timeout=None,
                    failed_attempts=None,
                    pass_timeout_times=None
                ):
        if service_config_id != SHA3_256(
            value = service_with_config.SerializeToString() # This service not touch metadata, so it can use the hash for id.
        ).hex():
            LOGGER('Service config not valid ', service_with_config, service_config_id)
            raise Exception('Service config not valid ', service_with_config, service_config_id)

        self.lock.acquire()
        self.services.update({
            service_config_id : ServiceConfig(
                service_with_config = service_with_config,
                service_hash = service_hash,
                stub_class = stub_class,
                timeout = timeout if timeout else self.timeout,
                failed_attempts = failed_attempts if failed_attempts else self.failed_attempts,
                pass_timeout_times = pass_timeout_times if pass_timeout_times else self.pass_timeout_times
            )
        })
        self.lock.release()
        try:
            LOGGER('ADDED NEW SERVICE ' + str(service_config_id) + ' \ndef_ids -> ' +  str(service_with_config.meta.hashtag.hash[0].value.hex()))
        except: LOGGER('ADDED NEW SERVICE ' + str(service_config_id))

    def get_service_with_config(self, service_config_id: str) -> gateway_pb2.ServiceWithConfig:
        return self.services[service_config_id].get_service_with_config()