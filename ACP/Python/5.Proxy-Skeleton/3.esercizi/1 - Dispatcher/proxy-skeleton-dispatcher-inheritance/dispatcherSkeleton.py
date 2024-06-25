from service_dispatcher import ServiceDispathcer
import socket as sk
from multiprocessing import Process

BUFFER_SIZE=1024

def skel_func(self, conn):
    data = conn.recv(BUFFER_SIZE)
    message = data.decode('utf-8')
    print(f'[SERVER] Ho ricevuto il messaggio: {message}')

    servizio = message.split('-')[0]

    if servizio == 'sendCmd':
        tipoCmd = message.split('-')[1]
        self.sendCmd(tipoCmd)
        backMessage = 'ACK'
    elif servizio == 'getCmd':
        backMessage = str(self.getCmd())
    
    retMessage = backMessage
    conn.send(retMessage.encode('utf-8'))
    
    conn.close()

    
        

class DispatcherSkeleton(ServiceDispathcer):
    """
        Classe che gestisce l'interfacciamento con i servizi del server
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def sendCmd(self, command):
        pass

    def getCmd(self):
        pass


    def run_skeleton(self):
        print("[SERVER] Avvio Skeleton...")
        print(f'[SERVER] Skeleton connesso con host: -{self.host}- e port: -{self.port}- ')
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.bind((self.host, self.port))

        print(f'[SERVER] In ascolto...')
        s.listen(30)

        while True:
            conn, addr = s.accept()
            print(f'[SERVER] Connesso con ({addr[0]}, {addr[1]})')

            p = Process(target = skel_func, args=(self, conn))
            p.start()




        
