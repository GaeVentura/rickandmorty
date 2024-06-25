from multiprocessing import Process
import socket
from IMagazzino import IMagazzino
from abc import abstractmethod

def p_func(self, conn):
    data = (conn.recv(1024).decode("utf-8"))
    print(f"[SERVER] RICEVUTO {data}")

    metodo = data.split('-')[0]
    ritorno = ""
    if metodo == "deposita":
        id = data.split('-')[1]
        ritorno = self.deposita(id)
    elif metodo == "preleva":
        id = data.split('-')[1]
        ritorno = self.preleva(id)

    ritorno = ritorno.encode("utf-8")

    conn.send(ritorno)

    conn.close()
        

class Skeleton(IMagazzino):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
    @abstractmethod
    def deposita(self, id):
        pass

    @abstractmethod
    def preleva(self, id):
        pass

    def runSkeleton(self):
        print(f"[SERVER] ACCENSIONE ")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, self.port))
        
        s.listen(10)

        while True:
            conn, addr = s.accept()
            p = Process(target = p_func, args = (self, conn))
            p.start()


