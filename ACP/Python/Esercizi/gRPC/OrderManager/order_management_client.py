import grpc, order_management_pb2, order_management_pb2_grpc

def run():

    with grpc.insecure_channel("localhost:58888") as channel:

        stub = order_management_pb2_grpc.OrderManagementStub(channel)
        ordini = []
        ordini.append(order_management_pb2.Order(items = ["cioccolata","cannella"], description = "buona", price = 3.54, destination = 'scozia'))
        
        lota = order_management_pb2.Order(description= "lota")
        risposta = stub.addOrder(lota)

        print(risposta)

        ricevuto = stub.getOrder(risposta)

        print(f"|{ricevuto.id}|{ricevuto.items}|{ricevuto.description}|{str(ricevuto.price)}|{ricevuto.destination}|")


if __name__ == "__main__":
    run()