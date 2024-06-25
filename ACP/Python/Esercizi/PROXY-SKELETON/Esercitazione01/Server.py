from IMagazzino import IMagazzino
from Magazzino import Magazzino

class Server(IMagazzino):
    def __init__(self, MagazzinoLaptop, MagazzinoSmartphone):
        self.MagazzinoLaptop = MagazzinoLaptop
        self.MagazzinoSmartphone = MagazzinoSmartphone


    # la coda circolare gestita come una lista

    def deposita(self, articolo, id):
        if articolo == "laptop":
            msg = self.MagazzinoLaptop.deposita(articolo,id)
        else:
            msg = self.MagazzinoSmartphone.deposita(articolo,id)
        
        return msg


    def preleva(self, articolo):
        if articolo == "laptop":
            msg = self.MagazzinoLaptop.preleva(articolo)
        else:
            msg = self.MagazzinoSmartphone.preleva(articolo)
        
        return msg



        