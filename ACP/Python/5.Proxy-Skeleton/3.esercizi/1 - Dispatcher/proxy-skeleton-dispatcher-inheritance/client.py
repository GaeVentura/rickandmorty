from dispatcherProxy import DispatcherProxy
import sys
import threading as thread
from random import randint

NUM_SEND = 3
def genera_richieste(host, port):
    for i in range(NUM_SEND):
        tipoCmd = randint(0,3)
        thread_name = thread.current_thread().name
        proxy = DispatcherProxy(host, port,thread_name)
        proxy.sendCmd(tipoCmd)


if __name__ == '__main__':
    try:
        host = sys.argv[1]
        port = sys.argv[2]
    except IndexError:
        print("Inserisci host e porta")
        sys.exit(-1)
    
    NUM_THREAD = 5
    thread_list = []

    for i in range(NUM_THREAD):
        t = thread.Thread(target = genera_richieste, args = (host, int(port)))
        t.start()
        thread_list.append(t)
    
    for i in range(NUM_THREAD):
        thread_list[i].join()