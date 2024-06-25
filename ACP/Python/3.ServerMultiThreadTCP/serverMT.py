import socket as socket
import threading as th

from threadTarget import thd_fun

if __name__ == '__main__':
    
    host = ""
    port = 12345

    # CREATE AND BIND A SOCKET

    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))

    s.listen(5)

    while True:
        
        # CONNESSIONE CON IL CLIENT
        c, addr = s.accept()

        # THREAD

        t = th.Thread(target=thd_fun, args=(c,))
        t.start()

    s.close()