# Si se toma una instancia, se debe de asegurar que, o bien se agrega a su cola
#  correspondiente, o bien se para. No asegurar esto ocasiona un bug importante,
#  ya que las instancias quedarían zombies en la red hasta que el servicio
#  fuera eliminado.
from datetime import datetime
from time import sleep

from gateway.communication import stop


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


