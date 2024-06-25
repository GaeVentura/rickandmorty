from abc import ABC,abstractmethod

class IDispatcher(ABC):

    @abstractmethod
    def sendCmd(self,command):
        pass
    
    @abstractmethod
    def getCmd(self):
        pass

