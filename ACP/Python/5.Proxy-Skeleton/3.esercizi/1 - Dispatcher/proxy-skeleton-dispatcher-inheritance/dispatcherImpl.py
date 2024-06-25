from dispatcherSkeleton import DispatcherSkeleton
from multiprocessing import Queue

class Dispatcher(DispatcherSkeleton):
    def __init__(self, host, port, queue):
        super().__init__(host, port)
        self.queue = queue
    
    def sendCmd(self, command):
        self.queue.put(command)
    
    def getCmd(self):
        return self.queue.get()
