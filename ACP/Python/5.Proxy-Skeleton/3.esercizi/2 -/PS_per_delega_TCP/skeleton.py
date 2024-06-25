from imagazzino import iMagazzino
import socket as sk
from multiprocessing import Process
from magazzinoImpl import Magazzino
from threading import Thread

BUFFER_SIZE = 1024
def skel_func(self, conn):
    data = (conn.recv(BUFFER_SIZE)).decode("utf-8")

    print(f'[SV] Ricevuta richiesta: {data}')
    servizio = data.split('-')[0]

    if servizio == "deposita":
        articolo = data.split('-')[1]
        id = data.split('-')[2]
        self.magazzino.deposita(articolo,id)
        riscontro = "ACK"
    elif servizio == "preleva":
        riscontro = self.magazzino.preleva(articolo)

    messaggio = riscontro
    print(f'[SV] Invio messaggio: {messaggio}')
    conn.send(messaggio.encode("utf-8"))

    conn.close()


class Skeleton(iMagazzino):
    def __init__(self, host, port, magazzino):
        self.host = host
        self.port = port
        self.magazzino = magazzino
    
    def deposita(self, articolo, id):
        self.magazzino.deposita(articolo,id)
    
    def preleva(self, articolo):
        return self.magazzino.preleva(articolo)

    def run_skeleton(self):
        

        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.bind((self.host,self.port))
        print(f'[SV] Avvio server...')

        s.listen(30)

        while True:
            conn, addr = s.accept()
            print(f'[SV] Aperta connessione con: ({addr[0]},{addr[1]})')
            
            t = Process(target = skel_func, args=(self,conn))
            print(f'Avvio..')
            t.start()





