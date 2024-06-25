import socket as sk

serverAddressPort = ("localhost".encode("utf-8"), 7000)
bufferSize = 1024

s = sk.socket(family = sk.AF_INET, type= sk.SOCK_DGRAM)
s.bind(serverAddressPort)
messaggioServer ="Ciao client \n"

while True:
    msgClient, addr = s.recvfrom(bufferSize)

    print(msgClient.decode("utf-8"))
    s.sendto(messaggioServer.encode("utf-8"), addr)

