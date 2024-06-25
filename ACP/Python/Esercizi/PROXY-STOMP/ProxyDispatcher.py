import socket
import time
from IMagazzino import IMagazzino
import stomp

class Proxy(IMagazzino):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def deposita(self, id):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        MSG = "deposita"+"-"+id
        data = MSG.encode("utf-8")
        s.send(data)
        print(f"[PROXY] INVIO MSG: {MSG}")
        ritorno = (s.recv(1024)).decode("utf-8")
        print(f"[PROXY] RICEVO MSG: {MSG}")
        s.close()
        return ritorno
    
    def preleva(self, id):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))

        MSG = "preleva"+"-"+id
        data = MSG.encode("utf-8")
        s.send(data)        
        print(f"[PROXY] INVIO MSG: {MSG}")

        ritorno = (s.recv(1024)).decode("utf-8")
        print(f"[PROXY] RICEVO MSG: {MSG}")

        return ritorno


class MyListener(stomp.ConnectionListener):
    def __init__(self, conn, proxy):
        self.conn = conn
        self.proxy = proxy
    
    def on_message(self, frame):
        print(f"[LISTENER] RECEIVED MESSAGE: {frame.body}")
        metodo = (frame.body).split('-')[0]
        ritorno = None
        if metodo == "deposita":
            id = (frame.body).split('-')[1]
            ritorno = self.proxy.deposita(id)
        elif metodo == "preleva":
            id = (frame.body).split('-')[1]
            ritorno = self.proxy.preleva(id)
        
        conn.send("queue/es2_Risposta", ritorno)
        print(f"[DISPATCHER] INVIO MSG: {ritorno}")
        


if __name__ == "__main__":
    proxy = Proxy("localhost", 56789)
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener('',MyListener(conn, proxy))
    conn.connect(wait=True)
    conn.subscribe(destination='queue/es2_Richiesta', id=1 , ack='auto')

    while True:
        print("[LISTENER] Attendo MSG")

        time.sleep(50)
