
import random
import statistics_pb2_grpc, statistics_pb2, grpc


if __name__ =="__main__":
    with grpc.insecure_channel("localhost:56789") as channel:

        stub = statistics_pb2_grpc.StatisticsStub(channel)

        for response in stub.getSensors(statistics_pb2.Empty()):

            print(f"[DASHBOARD] HO RICEVUTO ID {response._id}  CON DATA TYPE {response.data_type}")
            numRandInt = random.randint(0,1)

            if numRandInt == 0:
                data_type ="temp"
            else:
                data_type ="press"
            request = statistics_pb2.MeanRequest(sensor_id=response._id, data_type= response.data_type)

            print(f"[DASHBOARD] IL VALOR MEDIO E' {request.value}")

        





    