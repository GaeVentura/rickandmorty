from abc import ABC, abstractmethod

class IMagazzino(ABC):
    @abstractmethod
    def deposita(self, id):
        pass

    @abstractmethod
    def preleva(self, id):
        pass

