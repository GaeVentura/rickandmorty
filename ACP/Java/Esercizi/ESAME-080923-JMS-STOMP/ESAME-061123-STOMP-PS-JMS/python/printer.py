from multiprocessing import Condition, Lock, Process, Queue
from printerServer import PrinterSkeleton
import stomp
def send(msg:str):

    stompConn = stomp.Connection([('127.0.0.1', 61613)])

    stompConn.connect(wait = True)

    path, tipo = msg.split('-')

    stompConn.send(f"/queue/{tipo}", path)

    stompConn.disconnect()


class PrinterSem(PrinterSkeleton):

    def __init__(self, ):
        self.lock = Lock()
        self.queue = Queue()
        self.prod_cond = Condition(lock=self.lock)
        self.cons_cond = Condition(lock=self.lock)

    def print(self, pathFile: str, tipo: str):
        
        self.lock.acquire()

        while self.queue.full():
            self.prod_cond.wait()

        element = pathFile+"-"+tipo

        self.queue.put(element)

        print("[SERVER] HO MESSO ",element)

        self.cons_cond.notify()
        
        self.lock.release()
    
    def consumer(self,):
        
        while True:
            self.lock.acquire()
            print("[sono qui]")

            while self.queue.empty():
                self.cons_cond.wait()
            
            msg = self.queue.get()

            send(msg)

            print("[CONSUMER] HO INVIATO IL MSG: ", msg)

            self.prod_cond.notify()

            self.lock.release()


if __name__ =='__main__':

    printerSem = PrinterSem()

    p = Process(target= printerSem.consumer)
    p.start()

    printerSem.run_skeleton()

