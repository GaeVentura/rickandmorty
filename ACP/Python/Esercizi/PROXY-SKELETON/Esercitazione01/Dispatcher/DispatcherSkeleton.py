import socket
from IDispatcher import IDispatcher
from multiprocessing import Process



class DispatcherSkeleton(IDispatcher):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    
    def sendCmd(self,command):
        pass

    def getCmd(self):
        pass

    def runSkeleton(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((self.ip,self.port))

        s.listen(5)

        while True:
            conn, addr = s.accept()

            p = Process(target = proc_func, args =(self, conn, addr) )
            p.start()


def proc_func(self: DispatcherSkeleton,conn, addr):
    data = conn.recv(1024)
    print(data.decode("utf-8"))
    metodo = (data.decode("utf-8")).split("-")[0]
    msg = None
    if metodo == "sendCmd":
        comando = (data.decode("utf-8")).split("-")[1]
        msg = self.sendCmd(comando)
    elif metodo == "getCmd":
        msg = self.getCmd()
    else:
        msg ="Errore"
    
    conn.send(msg.encode("utf-8"))

    conn.close()






