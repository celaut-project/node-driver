# Demostracion de cola eficiente.
#  Se debe de colocar self.ram_pool = lambda: 10 
# # psutil.virtual_memory().available en RamLocker.__init__

from time import sleep
from iobigdata import IOBigData, mem_manager
from gas_manager import GasManager
from threading import Thread
import psutil

def p1():
    with mem_manager(len=7):
        sleep(6)
        print(1)

def p2():
    with mem_manager(len=9):
        sleep(3)
        print(2)

def p3():
    with mem_manager(len=3):
        sleep(3)
        print(3)

GasManager().put_initial_ram_pool(mem_limit = 10)
# IOBigData(ram_pool_method= lambda: psutil.virtual_memory().total) Simulacion de nodo.

Thread( target=p1 ).start()
sleep(1)
Thread( target=p2 ).start()
sleep(1)
Thread( target=p3 ).start()