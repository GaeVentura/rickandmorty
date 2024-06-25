from multiprocessing import Process, Queue, Semaphore
from LoggingServerSkeleton import LoggingServerSkeleton
import stomp


     

class LoggingServer(LoggingServerSkeleton):
    def __init__(self, port):
          super().__init__(port)
          self.queue = Queue(10)
          self.prod_sem = Semaphore(10)
          self.mutex_produttori = Semaphore(1)
          self.cons_sem = Semaphore(0)
          self.mutex_consumatori = Semaphore(1)
    
    def log(self, messaggioLog: str, tipo: int):
         
        self.prod_sem.acquire()

        with self.mutex_produttori:
            self.queue.put(f"{messaggioLog}-{str(tipo)}")
        
        self.cons_sem.release()
    
    def consumer(self):
         
         p = Process(target=proc_func,args=(self,))
         p.start()

def proc_func(logServ: LoggingServer ):

    stompConn = stomp.Connection([('127.0.0.1',61613)])
    stompConn.connect(wait = True)

    while True:
         
        logServ.cons_sem.acquire()

        with logServ.mutex_consumatori:

            MSG = logServ.queue.get()
        
        logServ.prod_sem.release()
        tipo = MSG.split('-')[1]

        if tipo == 2:
            stompConn.send("/queue/error", MSG)
        else: 
            stompConn.send("queue/info", MSG)

        print(f"[LOG-SERVER-CONSUMER] HO INVIATO IL MESSAGGIO: {MSG}")


if __name__ == "__main__":
    
    port = 56789
    logServer = LoggingServer(port)

    logServer.consumer()

    logServer.run_skeleton()
    