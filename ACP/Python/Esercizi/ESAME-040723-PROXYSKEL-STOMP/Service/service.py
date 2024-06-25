
import random


import socket

from ILogging import ILogging

class ServiceProxy(ILogging):

    def __init__(self, port):
        self.port = port

    def log(self, messaggioLog:str, tipo:int):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost", self.port))
        
        MSG = f"{messaggioLog}-{str(tipo)}"

        s.send(MSG.encode("utf-8"))



if __name__ == "__main__":

    sP = ServiceProxy(56789)
    for i in range(10):
        randomInteger = random.randint(0,3)
        messaggioLog:str
        if randomInteger == 0:
            messaggioLog = "success"
        elif randomInteger == 1:
            messaggioLog = "checking"
        elif randomInteger == 2:
            messaggioLog ="fatal"
        else:
            messaggioLog = "exception"
        
        sP.log(messaggioLog, randomInteger)
        


        



