
import uuid
import grpc
import order_management_pb2
import order_management_pb2_grpc
from concurrent import futures

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):
    def __init__(self):
        self.orders = {}

    
    def addOrder(self, request,context):
        id = uuid.uuid1()
        request.id = str(id)
        
        self.orders[request.id] = request

        ritorno = order_management_pb2.StringMessage(value = str(id))

        return ritorno

    def getOrder(self, request, context):

        order = self.orders.get(request.value)

        if order is not None:
            return order
        else:
            print('ORDER NOT FOUND' + request.value)
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Order '+ request.value+ ' not found')
            return order_management_pb2.Order()
        
    def searchOrders(self, request, context):
        itemDaCercare = request.value
        listaOrdiniPresenti = self.orders.value()
        listaOrdiniCorrispondenti = []
        for order in listaOrdiniPresenti:
            if listaOrdiniPresenti[order].items == itemDaCercare:
                listaOrdiniCorrispondenti.append(listaOrdiniPresenti[order])
        
        for order in listaOrdiniCorrispondenti:
            yield order

    def processOrders(self, request_iterator, context):


        listaDestinazioni = {}
        for order in request_iterator:
            if order.destination not in listaDestinazioni:
                listaDestinazioni[order.destination] = [order]
            else:
                listaDestinazioni[order.destination].append(order)
        
        for destination in listaDestinazioni.keys():
            ordini = listaDestinazioni[destination]
            spedizione = order_management_pb2.CombinedShipment(id = str(uuid.uuid3()), status= 'PROCESSED', orders = ordini)
            yield spedizione


def serve():
    port = "58888"

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)

    server.add_insecure_port("[::]:"+ port )
    print('Starting server. Listening on port ' + str(port))

    server.start()


    server.wait_for_termination()


if __name__ == "__main__":
    serve()
        