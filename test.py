# Demostracion de cola eficiente.
#  Se debe de colocar self.ram_pool = lambda: 10 
# # psutil.virtual_memory().available en RamLocker.__init__

from time import sleep
from iobigdata import IOBigData, mem_manager
from threading import Thread, Lock

RAM_POOL = 10
class NodeResourcesManagerSimulator:
    def __init__(self) -> None:
        self.ram_pool = RAM_POOL
        self.lock = Lock()

    def modify_resources(self, l):
        with self.lock:
            print('\n ei mai friend, yu want to change the ram, ok, i change it. ->  ', l, '\n')
            self.ram_pool = l
        return self.ram_pool

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

# IOBigData(ram_pool_method= lambda: psutil.virtual_memory().total) Simulacion de uso de la librería en nodo.

nrms = NodeResourcesManagerSimulator()
IOBigData(
    ram_pool_method = lambda: RAM_POOL,
    modify_resources= lambda l: nrms.modify_resources(l)['max']
)

Thread( target=p1 ).start()
sleep(1)
Thread( target=p2 ).start()
sleep(1)
Thread( target=p3 ).start()