from concurrent import futures
from pymongo import MongoClient
import statistics_pb2, statistics_pb2_grpc, grpc


def getDB():
    CONN_STR = "mongodb://127.0.0.1:27017"
    client = MongoClient(CONN_STR)
    return client['sensors']

class StatisticsServicer(statistics_pb2_grpc.StatisticsServicer):

    def getSensors(self, request, context):
        db = getDB()
        sensorsCollection = db['sensors']
        cursor = sensorsCollection.find()

        for i in cursor:
            yield statistics_pb2.Sensor( _id = i['_id'], data_type=i['data_type'])
    

    def getMean(self, request, context):
        db = getDB()
        data_type = request.data_type
        collection = db[data_type]

        cursor = collection.find({"sensor_id": f"{request.sensor_id}"})
        totale = 0
        for i in cursor:
            totale = totale + i["data"]
        
        media = totale/len(cursor)

        return statistics_pb2.StringMessage(value = str(media))


if __name__ == "__main__":

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    statistics_pb2_grpc.add_StatisticsServicer_to_server(StatisticsServicer(),server)

    server.add_insecure_port("[::]:56789")

    server.start()

    server.wait_for_termination()

    

        
