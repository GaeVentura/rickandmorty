from DispatcherSkeleton import DispatcherSkeleton
from multiprocessing import Condition, Lock, Queue

class DispatcherServer(DispatcherSkeleton):
    def __init__(self, ip, port):
        super().__init__(ip,port)

        self.cv_queue_lock = Lock()
        self.cv_prod = Condition(self.cv_queue_lock)
        self.cv_cons = Condition(self.cv_queue_lock)
        self.coda = Queue(5)

    def sendCmd(self,command):
        
        with self.cv_prod:
            while not spaceIsAvailable(self.coda):
                self.cv_prod.wait()
            
            self.coda.put(command)

            self.cv_cons.notify()
        
        return "MESSAGGIO DEPOSITATO"
    
    def getCmd(self):

        with self.cv_cons:
            while not anItemPresent(self.coda):
                self.cv_cons.wait()
            
            msg = self.coda.get()

            self.cv_prod.notify()

        return msg


def spaceIsAvailable(queue: Queue):
    bool = queue.full()
    return not bool

def anItemPresent(queue: Queue):
    bool = queue.empty()
    return not bool


if __name__ == "__main__":
    server = DispatcherServer('localhost', 56789)
    server.runSkeleton()