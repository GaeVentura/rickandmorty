
from concurrent import futures
import uuid
import order_management_pb2, order_management_pb2_grpc, grpc


class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):
    def __init__(self):
        self.storedOrders = {}

    def addOrder(self, request, context):
        id = uuid.uuid1()
        id = str(id)
        request.id = id
        self.storedOrders[id] = request

        backMessage = order_management_pb2.StringMessage(value = id)
        return backMessage
    
    def getOrder(self, request, context):
        
        if request.value in self.storedOrders:
            return self.storedOrders[request.value]
        else:
            print("[SERVER] getOrder: order NOT FOUND")
            order = order_management_pb2.Order()
        
    def searchOrders(self, request, context):
        itemToFind = request.value
        for key in self.storedOrders.keys():
            if itemToFind == self.storedOrders[key].items:
                yield self.storedOrders[key]
    
    def processOrders(self, request_iterator, context):
        dizionarioSpedizioni = {}

        for request in request_iterator:
            if request.destination not in dizionarioSpedizioni:
                dizionarioSpedizioni[request.destination] = [request]
            else:
                dizionarioSpedizioni[request.destination].append(request)

        for key in dizionarioSpedizioni.keys():
            idSped = uuid.uuid1()
            idSped = str(idSped)
            listaOrdini = dizionarioSpedizioni[key]
            statusSped = "PREPARED"

            yield order_management_pb2.CombinedShipment(
                id = idSped,
                status = statusSped,
                orders = listaOrdini
            )

def server():
    port = "56789"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)
    server.add_insecure_port("[::]:"+port)
    print('Starting server. Listening on port ' + str(port))

    server.start()


    server.wait_for_termination()

if __name__ == "__main__":
    server()