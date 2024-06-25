from datetime import datetime
from multiprocessing import Process
from random import randint
import socket
import time
from IDispatcher import IDispatcher

def client_func(proxy):

    waiting_time = randint(2,4)

    time.sleep(waiting_time)

    for i in range(3):

        comando = randint(0,3)

        messaggio = proxy.sendCmd(comando)

        print(f"[CLIENT] HO RICEVUTO {messaggio}")

def actuator_func(proxy):
    with open('cmdlog.txt', mode ='w') as log:
     while True:
        
            time.sleep(1)

            messaggio = proxy.getCmd()
            print(f"[ACTUATOR] HO RICEVUTO {messaggio}")
            log.write(f"{datetime.now()}: {messaggio}\n")




class ProxyDispatcher(IDispatcher):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
    def sendCmd(self, command):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        
        messaggio = "sendCmd" + "-"+str(command)
        s.send(messaggio.encode("utf-8"))

        data = s.recv(1024)
        s.close()
        return data.decode("utf-8")
    
    def getCmd(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        messaggio = "getCmd"
        s.send(messaggio.encode("utf-8"))

        data = s.recv(1024)
        s.close()
        return data.decode("utf-8")
    

if __name__ =="__main__":
    proxy = ProxyDispatcher("localhost", 56789)

    clientProcess = []
    actuatorProcess = None

    for i in range(5):
        p = Process(target = client_func, args=(proxy,))
        p.start()
        clientProcess.append(p)
    
    actuatorProcess = Process(target = actuator_func, args=(proxy,))
    actuatorProcess.start()



    


