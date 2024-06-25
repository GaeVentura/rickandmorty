from service_dispatcher import ServiceDispathcer
import socket as sk
import time
import random

BUFFER_SIZE = 1024

class DispatcherProxy(ServiceDispathcer):
    def __init__(self, host, port,nome_thread):
        self.host = host
        self.port = port
        self.nome_thread = nome_thread

    def sendCmd(self,command):
        
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.connect((self.host, self.port))
        
        message = "sendCmd-"+str(command)

        time.sleep(random.randint(2,4))

        s.send(message.encode('utf-8'))
        print(f'[CLIENTE - {self.nome_thread}] invio comando: {command}')

        data = (s.recv(BUFFER_SIZE)).decode('utf-8')

        print(f'[CLIENTE - {self.nome_thread}] ricevo messaggio: {data}')

        s.close()
        
    
    def getCmd(self):

        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.connect((self.host, self.port))

        message = "getCmd" 

        s.send(message.encode('utf-8'))
        data = s.recv(BUFFER_SIZE)

        return data.decode('utf-8')