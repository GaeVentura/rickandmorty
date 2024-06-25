from threading import Condition
from multiprocessing import Queue
from random import randint

def produzione(varcond_produttori, varcond_consumatori, codaElementi):
    
    with varcond_produttori:

        while not available_space(codaElementi):
            
            varcond_produttori.wait()

        insert_item(codaElementi)

        varcond_consumatori.notify()
        

def consumazione(varcond_produttori,varcond_consumatori, codaElementi):

    with varcond_consumatori:

        while not elements_in_queue(codaElementi):

            varcond_consumatori.wait()
        
        consume_item(codaElementi)

        varcond_produttori.notify()


            

# Ritorna True se c'è spazio disponibile, false altrimenti 
def available_space(codaElementi):
    return not codaElementi.full()

# Ritorna false se la coda è vuota,  true altrimenti 
def elements_in_queue(codaElementi):
    return not codaElementi.empty()

def insert_item(codaElementi):

    n = randint(1, 500)
    codaElementi.put(n)

    print("[Produttore] "+"Ho inserito: "+ str(n))

def consume_item(codaElementi):
    
    elemento = codaElementi.get()

    print("[CONSUMATORE] "+"Ho consumato: "+str(elemento))