import threading as th

from threading import Lock
from multiprocessing import Queue

from procedure import produzione, consumazione

NUM_PRODUTTORI = 10
NUM_CONSUMATORI = 10


codaElementi = Queue(0)

mutex_produttori = th.Semaphore(1)

prod_sem = th.Semaphore(5)

cons_sem = th.Semaphore(0)

mutex_consumatori = th.Semaphore(1)

thread_produttori = []
thread_consumatori = []

for i in range(NUM_PRODUTTORI):

    thread = th.Thread( target = produzione, args= ( codaElementi, prod_sem, cons_sem, mutex_produttori))
    thread.start()
    thread_produttori.append(thread)

for i in range(NUM_CONSUMATORI):

    thread = th.Thread( target = consumazione, args= ( codaElementi, prod_sem, cons_sem, mutex_consumatori))
    thread.start()
    thread_consumatori.append(thread)

for i in range(NUM_PRODUTTORI):

    thread_produttori[i].join()

for i in range(NUM_CONSUMATORI):

    thread_consumatori[i].join()
    