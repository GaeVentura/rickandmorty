from random import randint
from multiprocessing import Queue
from threading import Semaphore

def produzione( codaElementi, prod_sem, cons_sem, mutex_produttori):

        prod_sem.acquire()
        
        n = randint(1, 500)

        with mutex_produttori:
            
            codaElementi.put(n,)
            print("[PRODUTTORE] "+"Ho inserito: "+str(n))
        
        cons_sem.release()

def consumazione( codaElementi, prod_sem, cons_sem, mutex_consumatori):

        cons_sem.acquire()
        with mutex_consumatori:
            n = codaElementi.get()

            print("[CONSUMATORE]"+" Ho consumato: " + str(n) )

        prod_sem.release()
    






