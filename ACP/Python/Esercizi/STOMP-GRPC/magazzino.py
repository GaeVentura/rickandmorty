
from concurrent import futures
from multiprocessing import Queue, Semaphore
import magazzino_pb2, magazzino_pb2_grpc, grpc

class MagazzinoServicer(magazzino_pb2_grpc.MagazzinoServicer):
    def __init__(self):
        self.queue = Queue()
        self.prod_sem = Semaphore(5)
        self.cons_sem = Semaphore(0)
        self.mutex_prod = Semaphore(1)
        self.mutex_cons = Semaphore(1)

    def Preleva(self, request, context):
        self.cons_sem.acquire()

        with self.mutex_cons:
            prodotto = magazzino_pb2.Prodotto( id = self.queue.get().id, tipoProdotto= self.queue.get().tipoProdotto)

        self.prod_sem.release()
        return prodotto
    
    def Deposita(self, request, context):
        self.prod_sem.acquire()
        print("entro qui")
        with self.mutex_prod:
            print("entro pure qui")
            self.queue.put(request)

        self.cons_sem.release()    
        backMessage = magazzino_pb2.StringMessage(message="DEPOSITED ")

        return backMessage
    
    def Svuota(self, request, context):

        
        self.cons_sem.acquire()

        with self.cons_sem:
            for i in range(self.queue.qsize()):
                self.queue.get()
        
        backMessage = magazzino_pb2.StringMessage( message= "MAGAZZINO SVUOTATO")

        return backMessage
    

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    magazzino_pb2_grpc.add_MagazzinoServicer_to_server(MagazzinoServicer(), server)
    server.add_insecure_port("[::]:56789")



    server.start()
    print("[SERVER] ACCENSIONE...")
    server.wait_for_termination()

