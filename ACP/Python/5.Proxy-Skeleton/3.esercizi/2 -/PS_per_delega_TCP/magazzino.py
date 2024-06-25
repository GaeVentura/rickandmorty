from magazzinoImpl import Magazzino
from skeleton import Skeleton
from multiprocessing import Semaphore
from multiprocessing import Queue


DIM_CODA = 5

if __name__ == '__main__':
    host = 'localhost'
    port = 62121

    mutex_produttori = Semaphore(1)
    mutex_consumatori = Semaphore(1)

    cons_sem = Semaphore(1)
    prod_sem = Semaphore(DIM_CODA)

    coda_laptop = Queue(5)
    coda_smartphone = Queue(5)

    magazzino = Magazzino(coda_laptop, coda_smartphone, prod_sem, cons_sem, mutex_produttori, mutex_consumatori)
    skeleton = Skeleton(host, port, magazzino)
    skeleton.run_skeleton()
    