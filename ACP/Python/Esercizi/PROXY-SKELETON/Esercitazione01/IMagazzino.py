from abc import ABC, abstractmethod

class IMagazzino(ABC):
    @abstractmethod
    def deposita(articolo,id):
        pass
    
    @abstractmethod
    def preleva(articolo):
        pass
    

