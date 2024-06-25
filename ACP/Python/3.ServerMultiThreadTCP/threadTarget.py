
def thd_fun(c):

    data = c.recv(1024)

    c.send(data)

    c.close()