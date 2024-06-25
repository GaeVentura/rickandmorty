from imagazzino import iMagazzino
from procedure import produzione, consumazione

class Elemento():
    def __init__(self, articolo, id):
        self.articolo = articolo
        self.id = id

class Magazzino(iMagazzino):
    def __init__(self, coda_laptop, coda_smartphone, prod_sem, cons_sem, mutex_produttori, mutex_consumatori ):
        self.coda_laptop = coda_laptop
        self.coda_smartphone = coda_smartphone
        self.prod_sem=prod_sem
        self.cons_sem=cons_sem
        self.mutex_produttori=mutex_produttori
        self.mutex_consumatori=mutex_consumatori

    def deposita(self, articolo, id):
        elemento = Elemento(articolo, id)
        if elemento.articolo == "laptop":
            produzione(self.coda_laptop, self.prod_sem, self.cons_sem, self.mutex_produttori, elemento)
        elif elemento.articolo == "smartphone":
            produzione(self.coda_smartphone, self.prod_sem, self.cons_sem, self.mutex_produttori, elemento)

    def preleva(self, articolo):
        if articolo =="laptop":
            elemento = consumazione(self.coda_laptop, self.prod_sem, self.cons_sem, self.mutex_consumatori)
        elif articolo =="smartphone":
            elemento = consumazione(self.coda_laptop, self.prod_sem, self.cons_sem, self.mutex_consumatori)
        
        prelevato = elemento.id

        return prelevato
