# I/O Big Data utils.
import gc
from time import sleep
from threading import Lock
import gas_manager as gm

from utils import Singleton

mem_manager = lambda len: IOBigData().lock(len=len)
class IOBigData(metaclass=Singleton):

    class RamLocker(object):
        def __init__(self, len, iobd):
            self.len = len
            self.iobd = iobd

        def __enter__(self):
            self.iobd.lock_ram(ram_amount = self.len)
            return self

        def unlock(self, amount: int):
            self.iobd.unlock_ram(ram_amount = amount)
            self.len -= amount

        def __exit__(self, type, value, traceback):
            self.iobd.unlock_ram(ram_amount = self.len)
            gc.collect()

    def __init__(self, 
            log = lambda message: print(message),
            ram_pool_method = None   # Will be None if it's used by a service.
        ) -> None:
        if ram_pool_method:
            self.ram_pool = ram_pool_method
            self.push_gas_wait = lambda len: len  # Don't work.
            self.pop_gas_wait = lambda len: len  # Don't work.
            self.get_wait_amount = lambda: 'Unknown'
        else:
            self.ram_pool = lambda : gm.GasManager().get_ram_pool()
            self.push_gas_wait = lambda len: gm.GasManager().push_wait_list(mem_limit=len)
            self.pop_gas_wait = lambda len: gm.GasManager().pop_wait_list(mem_limit=len)
            self.get_wait_amount = lambda: IOBigData.convert_size(sum(gm.GasManager().wait))

        self.log = log
        self.ram_locked = 0
        self.get_ram_avaliable = lambda: self.ram_pool() - self.ram_locked
        self.amount_lock = Lock()

    def set_log(self, log = lambda message: print(message)) -> None:
        self.log = log

    @staticmethod
    def convert_size(size_bytes):
        import math
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    def stats(self, message: str):
        with self.amount_lock:
            self.log('\n--------- '+message+' -------------')
            self.log('RAM POOL       -> '+ IOBigData.convert_size(self.ram_pool()))
            self.log('RAM LOCKED     -> '+ IOBigData.convert_size(self.ram_locked))
            self.log('RAM AVALIABLE  -> '+ IOBigData.convert_size(self.get_ram_avaliable()))
            self.log('For gas manager: RAM WAITING      '+ self.get_wait_amount())
            self.log('-----------------------------------------\n')

    def lock(self, len):
        return self.RamLocker(len = len, iobd = self)

    def lock_ram(self, ram_amount: int, wait: bool = True):
        self.stats('want lock ' + IOBigData.convert_size(ram_amount))
        self.push_gas_wait(len=ram_amount)
        while True:
            self.stats('go to lock ' + IOBigData.convert_size(ram_amount))
            if wait:
                self.wait_to_prevent_kill(len = ram_amount)

            elif not self.prevent_kill(len = ram_amount):
                self.pop_gas_wait(len=ram_amount)
                raise Exception

            with self.amount_lock:
                if self.get_ram_avaliable() > ram_amount:
                    self.pop_gas_wait(len=ram_amount)
                    self.ram_locked += ram_amount
                    break
                else:
                    continue
        self.stats('locked')

    def unlock_ram(self, ram_amount: int):
        with self.amount_lock:
            if ram_amount < self.ram_locked:
                self.ram_locked -= ram_amount
            else:
                self.ram_locked = 0
        self.stats('unlocked')

    def prevent_kill(self, len: int) -> bool:
        with self.amount_lock:
            b = self.get_ram_avaliable() > len
        return b

    def wait_to_prevent_kill(self, len: int) -> None:
        while True:
            if not self.prevent_kill(len = len):
                sleep(1)
            else:
                return
