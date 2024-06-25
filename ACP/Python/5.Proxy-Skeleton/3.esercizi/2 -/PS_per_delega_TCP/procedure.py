from multiprocessing import Queue
from threading import Semaphore

def produzione( codaElementi, prod_sem, cons_sem, mutex_produttori, elemento):

    prod_sem.acquire()

    with mutex_produttori:

        codaElementi.put(elemento)
    
    cons_sem.release()

def consumazione( codaElementi, prod_sem, cons_sem, mutex_consumatori):

    cons_sem.acquire()

    with mutex_consumatori:

        elemento = codaElementi.get()
    
    prod_sem.release()

    return elemento