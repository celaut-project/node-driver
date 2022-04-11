from threading import Lock
from utils import Singleton
class GasManager(metaclass=Singleton):

    def __init__(self) -> None:
        self.loop_sleep_time = 60
        self.ram_pool = 0
        self.gas = 20  # TODO will be a polynomy.
        self.wait = []
        self.wait_lock = Lock()

    # When the service starts, it take that from __config__.
    def put_initial_ram_pool(self, mem_limit: int):
        self.ram_pool = mem_limit

    # For the start method of each service.
    def put_gateway_interface(
        self,
        modify_resources,
        get_resources,
    ):
        self.modify_resources = modify_resources
        self.get_resources = get_resources

    # For iobigdata.
    def push_wait_list(self, mem_limit: int):
        with self.wait_lock:
            self.wait.append(mem_limit)
        #if self.gas < sum(self.wait)
        # Si supera cierto límite de espera, aumenta con modify_resources()

    def pop_wait_list(self, mem_limit: int):
        with self.wait_lock:
            self.wait.remove(mem_limit)

    def get_ram_pool(self) -> int:
        return self.ram_pool