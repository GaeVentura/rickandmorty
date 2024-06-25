from concurrent import futures
from pymongo import MongoClient
import statistics_pb2,statistics_pb2_grpc, grpc



def getDatabase():

    CONNECTION_STRING = "mongodb://127.0.0.1:27017"

    db = MongoClient(CONNECTION_STRING)

    return db['test']

class StatisticsServicer(statistics_pb2_grpc.StatisticsServicer):

    def getSensors(self, request, context):
        
        print("[da verificare] get sensors")

        db = getDatabase()

        sensors = db['sensors']

        for i in range(5):
            back = sensors.find({'id':f'S{i}' })
            yield statistics_pb2.Sensor(id = back['_id'], dataTipe=back['data_type'] )

    def getMean(self, request, context):
        
        db = getDatabase()

        dataTypeCollection = db[request.dataType]

        result = dataTypeCollection.find({"sensor_id": request.id})

        totale:int 

        for i in result:
            totale = totale + result['data']

        media = totale / len(result)

        return statistics_pb2.StringMessage(value= str(media))
    


if __name__ =="__main__":

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    statistics_pb2_grpc.add_StatisticsServicer_to_server(StatisticsServicer(), server)

    server.add_insecure_port("[::]:56789")

    server.start()

    print("[STATISTICS] IN ACCENSIONE")

    server.wait_for_termination()

