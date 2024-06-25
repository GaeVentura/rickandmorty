from IMagazzino import IMagazzino

class Magazzino(IMagazzino):
    def __init__(self,
                 nome,
                 coda,
                 prod_sem, 
                 cons_sem, 
                 mutex_prod):
        
        self.nome = nome
        self.coda = coda
        self.prod_sem = prod_sem
        self.cons_sem = cons_sem
        self.mutex_prod = mutex_prod
        self.index_prod = 0
        self.index_cons = 0
    
    def deposita(self, articolo, id):
        self.prod_sem.acquire()
        elemento = id
        with self.mutex_prod:
            self.coda[self.index_prod] = elemento
            print(f"[{self.nome}] Ho aggiunto l'articolo con id: {id}")
            self.index_prod = (self.index_prod + 1 ) % 5      
        
        self.cons_sem.release()

        return "ok"
    
    def preleva(self, articolo):
        self.cons_sem.acquire()
       
        id = self.coda[self.index_cons]
        self.index_cons = (self.index_cons +1) % 5
        print(f"[{self.nome}] Ho prelevato: {str(id)}")
        
        self.prod_sem.release()
        return str(id)




