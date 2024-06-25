
import threading as th
from threading import Lock, Condition
from procedure import produzione, consumazione

from multiprocessing import Queue

NUM_CONSUMATORI = 10
NUM_PRODUTTORI = 10

threads_produttori = []
threads_consumatori = []

varcond_produttori_lock = Lock()
varcond_consumatori_lock = Lock()

varcond_produttori = Condition( varcond_produttori_lock)
varcond_consumatori = Condition( varcond_consumatori_lock)

codaElementi = Queue(5)

for i in range(NUM_PRODUTTORI):
    
    t = th.Thread( target=produzione, args=(varcond_produttori, varcond_consumatori, codaElementi))
    t.start()
    threads_produttori.append(t)

for i in range(NUM_CONSUMATORI):
    
    t = th.Thread( target=consumazione, args=(varcond_produttori, varcond_consumatori, codaElementi))
    t.start()
    threads_consumatori.append(t)   

for i in range(NUM_PRODUTTORI):
    
    threads_produttori[i].join()


for i in range(NUM_CONSUMATORI):
    
    threads_consumatori[i].join()   
