from datetime import timedelta, datetime
from threading import Thread, Lock
from time import sleep

from celaut_framework.dependency_manager.service_config import ServiceConfig
from celaut_framework.gateway.communication import generate_gateway_stub
from celaut_framework.gateway.protos import gateway_pb2
from celaut_framework.dependency_manager.service_interface import ServiceInterface
from celaut_framework.protos import celaut_pb2
from celaut_framework.utils.lambdas import SHA3_256
from celaut_framework.utils.lambdas import LOGGER
from celaut_framework.utils.singleton import Singleton

MAINTENANCE_SLEEP_TIME_DEFAULT = 60
TIMEOUT_DEFAULT = 30
FAILED_ATTEMPTS_DEFAULT = 20
PASS_TIMEOUT_TIMES_DEFAULT = 5

class DependencyManager(metaclass = Singleton):

    def __init__(self,
                 gateway_main_dir: str,
                 static_service_directory: str,
                 dynamic_service_directory: str,
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
        self.static_service_directory = static_service_directory
        self.dynamic_service_directory = dynamic_service_directory

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
                    service_hash: str,
                    config: celaut_pb2.Configuration,
                    stub_class,
                    dynamic: bool,
                    timeout: int = None,
                    failed_attempts: int = None,
                    pass_timeout_times: int = None
                    ) -> ServiceInterface:
        
        if not config:
            config = celaut_pb2.Configuration()
            
        service_config_id: str = SHA3_256(
            bytes(service_hash, 'utf-8') + SHA3_256(
                config.SerializeToString()
            )
        ).hex()
        self.lock.acquire()
        service_config = ServiceConfig(
                service_hash = service_hash,
                config = config,
                stub_class = stub_class,
                timeout = timeout if timeout else self.timeout,
                failed_attempts = failed_attempts if failed_attempts else self.failed_attempts,
                pass_timeout_times = pass_timeout_times if pass_timeout_times else self.pass_timeout_times,
                dynamic = dynamic,
                dev_client = self.dev_client,
                static_service_directory = self.static_service_directory,
                dynamic_service_directory = self.dynamic_service_directory
            )
        self.services.update({
            service_config_id : service_config
        })
        self.lock.release()
        
        return ServiceInterface(
            service_with_config = service_config,
            gateway_stub = self.gateway_stub
        )
        

    def get_service_with_config(self, service_config_id: str) -> gateway_pb2.ServiceWithConfig:
        return self.services[service_config_id].get_service_with_config()