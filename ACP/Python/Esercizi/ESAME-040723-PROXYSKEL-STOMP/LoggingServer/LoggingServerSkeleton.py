from multiprocessing import Process
import socket
from ILogging import ILogging
from abc import abstractmethod

def proc_func(conn:socket, LoggingServer:ILogging):
    data = conn.recv(1024).decode("utf-8")
    
    messaggioLog = data.split('-')[0]
    tipo = int(data.split('-')[1])

    LoggingServer.log(messaggioLog,tipo)

    


class LoggingServerSkeleton(ILogging):

    def __init__(self, port):
        self.port = port

    @abstractmethod
    def log(self, messaggioLog:str, tipo:int):
        pass

    def run_skeleton(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("localhost", self.port))
        s.listen()

        print("[SERVER] AVVIATO")
        while True:

            conn, addr = s.accept()
            
            p = Process(target=proc_func, args = (conn, self))
            p.start()

