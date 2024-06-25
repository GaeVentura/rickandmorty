from multiprocessing import Process
import time, stomp
import magazzino_pb2_grpc, magazzino_pb2, grpc

def proc_func(message, stub:magazzino_pb2_grpc.MagazzinoStub, conn:stomp.Connection):
    tipo_richiesta = message.split('-')[0]
    print(tipo_richiesta)
    if tipo_richiesta == "deposita":
        id_articolo = message.split('-')[1]

        tipo_prodotto = message.split('-')[2]

        prodotto = magazzino_pb2.Prodotto(id=id_articolo, tipoProdotto=tipo_prodotto)
        backMessage:magazzino_pb2.StringMessage = stub.Deposita(prodotto)
        conn.send('/queue/response_queue', backMessage.message)
    
    elif tipo_richiesta == "preleva":
        #id_articolo = message.split('-')[1]
        MSG = magazzino_pb2.StringMessage()#message=id_articolo)
        prodotto:magazzino_pb2.Prodotto = stub.Preleva(MSG)
        backMessage = prodotto.id+"-"+prodotto.tipoProdotto
        conn.send('/queue/response_queue', backMessage)

    else:
        
        MSG = magazzino_pb2.StringMessage(message=tipo_richiesta)
        backMessage:magazzino_pb2.StringMessage = stub.Svuota(MSG)
        conn.send('/queue/response_queue', backMessage.message)

    



class MyListener(stomp.ConnectionListener):
    def __init__(self, conn, stub):
        self.conn = conn
        self.stub = stub

    def on_message(self, frame):
        message = frame.body
        p = Process(target= proc_func, args=(message, self.stub, self.conn))
        p.start()



if __name__ =="__main__":
    channel = grpc.insecure_channel('localhost:56789')
    stub = magazzino_pb2_grpc.MagazzinoStub(channel)

    stompConn = stomp.Connection([('127.0.0.1',61613)])
    stompConn.set_listener('', MyListener(stompConn,stub))

    stompConn.connect(wait=True)
    stompConn.subscribe(destination = "/queue/request_queue", id = 1, ack ='auto')

    print("[DISPATCHER] Waiting for request")

    time.sleep(15)

    stompConn.disconnect()
