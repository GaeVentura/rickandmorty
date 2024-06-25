import socket as sk
import sys

def client(port):

    serverAddressPort=("localhost".encode("utf-8"), port)
    bufferSize = 1024 

    s = sk.socket( family=sk.AF_INET, type= sk.SOCK_DGRAM)

    msgClient="Ciao server \n"
    s.sendto(msgClient.encode("utf-8"), serverAddressPort)

    s.close()

if __name__ =="__main__":
    try:
        port = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg...")
    
    assert port !="", 'specify port'
    client(int(port))