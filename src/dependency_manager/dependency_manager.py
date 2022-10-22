from datetime import timedelta, datetime
from threading import Thread, Lock
from time import sleep

from dependency_manager.service_config import ServiceConfig
from gateway.communication import generate_gateway_stub
from gateway.protos import gateway_pb2
from utils.lambdas import LOGGER, SHA3_256
from utils.singleton import Singleton

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
                 pass_timeout_times: int = PASS_TIMEOUT_TIMES_DEFAULT,
                 dev_client: str = None,
            ):

        self.maintenance_sleep_time = maintenance_sleep_time
        self.timeout = timeout
        self.failed_attempts = failed_attempts
        self.pass_timeout_times = pass_timeout_times

        self.dev_client = dev_client

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
                    dynamic: bool,
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
                pass_timeout_times = pass_timeout_times if pass_timeout_times else self.pass_timeout_times,
                dynamic = dynamic,
                dev_client = self.dev_client
            )
        })
        self.lock.release()
        try:
            LOGGER('ADDED NEW SERVICE ' + str(service_config_id) + ' \ndef_ids -> ' +  str(service_with_config.meta.hashtag.hash[0].value.hex()))
        except: LOGGER('ADDED NEW SERVICE ' + str(service_config_id))

    def get_service_with_config(self, service_config_id: str) -> gateway_pb2.ServiceWithConfig:
        return self.services[service_config_id].get_service_with_config()