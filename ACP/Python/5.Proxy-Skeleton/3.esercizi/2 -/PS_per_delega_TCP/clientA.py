import threading as th
from magazzinoProxy import Proxy
from random import randint

N_RICHIESTE = 3
def ClientA_func(host,port):
    for i in range(N_RICHIESTE):
        thread_name = th.current_thread().name
        proxy = Proxy(host, port, thread_name, i)
        id = randint(1,100)
        articoli = {'1':'laptop', '2':'smarthphone'}
        a_caso = randint(1,2)
        articolo = articoli[str(a_caso)]

        proxy.deposita(articolo, id)

N_THREAD = 1
if __name__ == '__main__':
    host = 'localhost'
    port = 62121

    ClientA_threads = []

    for i in range(N_THREAD):
        t = th.Thread(target = ClientA_func, args = (host, port))
        t.start()
        ClientA_threads.append(t)

    for i in range(N_THREAD):
        ClientA_threads[i].join()
    
    