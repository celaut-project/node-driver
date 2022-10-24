from dependency_manager.service_instance import ServiceInstance

from dependency_manager.service_config import ServiceConfig


class ServiceInterface:

    def __init__(self,
                 gateway_stub,
                 service_with_config: ServiceConfig
                 ):
        self.gateway_stub = gateway_stub
        self.sc = service_with_config


    def get_instance(self) -> ServiceInstance:
        self.sc.lock.acquire()

        try:
            instance = self.sc.get_instance()
            self.sc.lock.release()

        except IndexError:
            self.sc.lock.release()
            instance = self.sc.launch_instance(
                self.gateway_stub
            )

        instance.mark_time()
        return instance

    def push_instance(self, instance: ServiceInstance):

        if instance.is_zombie(
            pass_timeout_times = self.sc.pass_timeout_times,
            timeout = self.sc.timeout,
            failed_attempts = self.sc.failed_attempts
        ):
            instance.stop(
                self.gateway_stub
            )

        else:
            self.sc.lock.acquire()
            self.sc.add_instance(
                instance = instance
            )
            self.sc.lock.release()