from imagazzino import iMagazzino
import socket as sk
import time 
import random

BUFFER_SIZE = 1024
class Proxy(iMagazzino):
    def __init__(self, host, port, thread_name, request_number):
        self.host = host
        self.port = port
        self.thread_name = thread_name
        self.request_number = request_number

    def deposita(self, articolo, id):
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        s.connect((self.host, self.port))

        request = 'deposita'
        message_to_send = request + '-' + str(articolo) + '-' + str(id)
        
        time.sleep(random.randint(2,4))
        print(f'[CLIENTA] invio richiesta {message_to_send} dal {self.thread_name} con richiesta Num: {self.request_number}\n')
        s.send(message_to_send.encode("utf-8"))

        data = (s.recv(BUFFER_SIZE)).decode('utf-8')
        print(f'[CLIENT] - {self.thread_name} - ricevuto riscontro {data}\n')


    def preleva(self, id):
        s = socket(sk.AF_INET, sk.SOCK_STREAM)
        s.connect((self.host, self.port))

        request = 'preleva'
        message_to_send = request +'-'+ str(id)

        s.send(message_to_send.encode('utf-8'))

        data = s.recv(BUFFER_SIZE)

