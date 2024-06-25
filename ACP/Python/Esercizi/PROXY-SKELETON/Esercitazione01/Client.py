
import socket
import time
from IMagazzino import IMagazzino
from random import randint
from threading import Thread

def deposita(articolo, id, proxy):
    waiting_time = randint(2, 4)
    time.sleep(waiting_time)

    proxy.deposita(articolo, id)

def preleva(articolo, proxy):
    waiting_time = randint(2, 4)
    time.sleep(waiting_time)
    proxy.preleva(articolo)
    

class Proxy(IMagazzino):
    def __init__(self, port):
        self.port = port

    def deposita(self,articolo, id):
        ip='localhost'
        BUFFER_SIZE = 1024 
        message = "deposita-"+articolo+"-"+str(id)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip, self.port))
        s.send(message.encode("utf-8"))
        data = s.recv(BUFFER_SIZE)
        print(f"[DEPOSITA] Ho ricevuto {str(data)}") 
        s.close

    def preleva(self, articolo):
        ip = 'localhost'
        BUFFER_SIZE = 1024
        message = "preleva-"+articolo

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, self.port))
        s.send(message.encode("utf-8"))
        data = s.recv(BUFFER_SIZE)
        print(f"[PRELEVA] ho prelevato: {data}")



if __name__ == "__main__":
    prodThreadList = []
    consThreadList = []
    proxy = Proxy(57986)

    for i in range(5):
        articoloCaso = randint(1,2)
        articolo = None
        if articoloCaso == 1:
            articolo = "laptop"
        else:
            articolo = "smartphone"
        
        id = randint(1,100)
        t = Thread(target = deposita, args = (articolo, id, proxy))
        t.start()
        prodThreadList.append(t)

    for i in range(5):
        articoloCaso = randint(1,2)
        articolo = None
        if articoloCaso == 1:
            articolo = "laptop"
        else:
            articolo = "smartphone"
        
        t = Thread(target = preleva, args = (articolo, proxy))
        t.start()
        consThreadList.append(t)

    for i in range(5):
        prodThreadList[i].join()
    
    for i in range(5):
        consThreadList[i].join()
    

        
    
    
        
