
from multiprocessing import Process
import socket
from IPrinter import IPrinter
from abc import abstractmethod

def proc_func(printer:IPrinter, conn):
    msg = conn.recv(1024).decode('utf-8')
    path, tipo= msg.split('-')
    
    printer.print(path, tipo)





class PrinterSkeleton(IPrinter):

    @abstractmethod
    def print(self, pathFile: str, tipo: str):
        pass


    def run_skeleton(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', 56789))
        s.listen()
        print("[SERVER] AVVIATO SERVER")
        while True:

            conn, addr = s.accept()
            p = Process(target = proc_func, args=(self, conn))
            p.start()
