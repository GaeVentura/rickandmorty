from abc import ABC, abstractmethod

class ServiceDispathcer(ABC):
    
    @abstractmethod
    def sendCmd(self, command):
        pass

    @abstractmethod
    def getCmd(self):
        pass