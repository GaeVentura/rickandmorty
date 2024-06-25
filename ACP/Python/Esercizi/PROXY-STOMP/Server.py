from multiprocessing import Queue, Semaphore
from ServerSkeleton import Skeleton

class Dispatcher(Skeleton):
    def __init__(self, ip, port):
        super().__init__(ip,port)
        self.queue = Queue(5)
        self.prod_sem = Semaphore(5)
        self.mutex_prod = Semaphore(1)
        self.cons_sem = Semaphore(0)
        self.mutex_cons = Semaphore(1)
    
    def deposita(self, id):        
        self.prod_sem.acquire()

        with self.mutex_prod:
            self.queue.put(id)
            print(f"[SERVER] HO DEPOSITATO {id}")
        
        self.cons_sem.release()

        return "deposited"
    

    def preleva(self, id):

        self.cons_sem.acquire()
        
        with self.mutex_cons:
            ritorno = self.queue.get()

        self.prod_sem.release()

        return ritorno


if __name__ =="__main__":
    ip = "localhost"
    port = 56789

    server = Dispatcher(ip, port)

    server.runSkeleton()

