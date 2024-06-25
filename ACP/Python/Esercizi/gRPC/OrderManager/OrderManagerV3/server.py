from concurrent import futures
import uuid
import grpc
import order_management_pb2, order_management_pb2_grpc


class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):

    orderNoteBook = {}

    def addOrder(self, request, context):
        id = str (uuid.uuid1())
        request.id = id
        self.orderNoteBook[id] = request

        backMessage = order_management_pb2.StringMessage( value = id)

        return backMessage


    def getOrder(self, request, context):

        if id in self.orderNoteBook:
            return self.orderNoteBook[id]
        else:
            return order_management_pb2.Order()


    def searchOrders(self, request, context):
    
        toFind = request.value
        

        for id, order in self.orderNoteBook.items():



            
            listItem = order.items

            for i in listItem:

                if i == toFind:
                    yield order

    
    def processOrders(self, request_iterator, context):
        
        listaDestinazioni = {}
        for request in request_iterator:
            
            if request.destination not in listaDestinazioni:
                
                listaDestinazioni[request.destination] = [request]
            
            else:
                listaDestinazioni[request.destination].append(request)
        
        for key in listaDestinazioni:
            idShipment = str(uuid.uuid4())
            shipment = order_management_pb2.CombinedShipment( id = idShipment, status="PREPARED", orders = listaDestinazioni[key])

            yield shipment

    

if __name__ == "__main__":

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)

    server.add_insecure_port("[::]:56789")

    server.start()

    print("[SERVER] IN ACCENSIONE")

    server.wait_for_termination()


            
