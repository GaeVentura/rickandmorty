import socket
from IMagazzino import IMagazzino
from threading import Thread
from threading import Semaphore
from Magazzino import Magazzino
from Server import Server
def thd_func(c,self):
    data = c.recv(1024)
    metodo = (data.decode('utf-8')).split('-')[0]
    if metodo == 'deposita':
        articolo = (data.decode('utf-8')).split('-')[1]
        id = (data.decode('utf-8')).split('-')[2]
        result = self.subject.deposita(articolo,id)
    if metodo == 'preleva':
        articolo = (data.decode('utf-8')).split('-')[1]
        result = self.subject.preleva(articolo)
    print(result)
    result = result.encode("utf-8")
    c.send(result)
    c.close




# PATTERN SKELETON
s_n = "[SERVER SKELETON]"
class Skeleton(IMagazzino):


    def __init__(self,port,subject):
        self.port = port
        self.subject = subject
    
    def deposita(self,articolo,id):
        return self.subject.deposita(articolo,id)
    
    def preleva(self,articolo):
        return self.subject.preleva(articolo)
    
    def run_skeleton(self):
        host='localhost'

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host,self.port))
        self.port = s.getsockname()[1]

        #print(f"{s_n} binded to port: {str(self.port)} ")

        s.listen(5)
        #print(f"{s_n} is listening")

        while True:
            c,addr = s.accept()
            #print(f"{s_n} connected to {addr[0]} : {addr[1]}")

            t = Thread(target=thd_func, args=(c,self))
            t.start()

if __name__ == "__main__":

    try:
        PORT = 57986
    except IndexError:
        print("Please, specify PORT arg")
    
    print("Server running")
    prod_sem_laptop = Semaphore(5)
    cons_sem_laptop = Semaphore(0)
    mutex_prod_laptop = Semaphore()
    coda_laptop = [0,0,0,0,0]
    prod_sem_smartphone = Semaphore(5)
    cons_sem_smartphone = Semaphore(0)
    mutex_prod_smartphone = Semaphore()
    coda_smartphone = [0,0,0,0,0]
    MagazzinoSmartphone = Magazzino("Magazzino Smartphone", coda_smartphone, prod_sem_smartphone, cons_sem_smartphone, mutex_prod_smartphone)
    MagazzinoLaptop = Magazzino("Magazzino Laptop", coda_laptop, prod_sem_laptop, cons_sem_laptop, mutex_prod_laptop)
    server = Server(MagazzinoLaptop, MagazzinoSmartphone)
    skeleton = Skeleton(int(PORT), server)
    skeleton.run_skeleton()
