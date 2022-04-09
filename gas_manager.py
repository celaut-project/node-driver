from utils import Singleton
class GasManager(metaclass=Singleton):

    def __init__(self) -> None:
        self.ram_pool = 0
        self.gas = 0  # TODO will be a polynomy.

    # When the service starts, it take that from __config__.
    def put_initial_ram_pool(self, mem_limit: int):
        self.ram_pool = mem_limit

    def get_ram_pool(self) -> int:
        return self.ram_pool