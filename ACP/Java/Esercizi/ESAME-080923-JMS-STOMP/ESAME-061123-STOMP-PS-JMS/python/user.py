import random
import socket
from IPrinter import IPrinter

class UserProxy(IPrinter):

    def print(self, pathFile: str, tipo: str):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(('localhost', 56789))

        MSG = pathFile +"-"+tipo

        s.send(MSG.encode("utf-8"))




if __name__ == "__main__":
    num_richieste = 10
    proxy = UserProxy()

    for i in range(num_richieste):
        randomInteger = random.randint(0,2)
        tipo: str
        if randomInteger == 0:
            tipo = 'bw'
        elif randomInteger == 1:
            tipo = 'gs'
        else:
            tipo = 'color'
        
        NUM = random.randint(0,100)
        estensione :str
        if NUM < 50:
            estensione ='txt'
        else:
            estensione ='doc'

        pathFile = f"/user/file_{NUM}.{estensione}"

        proxy.print(pathFile, tipo)
    
    
        

