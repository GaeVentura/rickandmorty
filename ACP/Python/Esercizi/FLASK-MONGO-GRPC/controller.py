
from flask import Flask, request
from pymongo import MongoClient
import pymongo
import pymongo.errors

app = Flask(__name__)


def getDatabase():
    CONNECTION_STRING ="mongodb://127.0.0.1:27017"
    client = MongoClient(CONNECTION_STRING)

    return client['test']


@app.post("/sensor")
def recSensor():

    try:
        sensor = request.get_json()
        print(sensor)
        db = getDatabase()
        collection = db['sensors']

        collection.insert_one(sensor)
        
        return {'result':'success'}
    except pymongo.errors.DuplicateKeyError:
        return {'result': 'failed, è stato già aggiunto questo sensore'}
    except:
        return {'result': 'failed, ma non so cosa è successo'}




@app.post("/data/<data_type>")
def getData(data_type):
    db = getDatabase()
    json = request.get_json()
    if data_type == "temp":

        collection = db['temp']

        collection.insert_one(json)
        return {'result':'success'}
    elif data_type == "press":

        collection = db['press']
        collection.insert_one(json)
        return {'result':'success'}
    else:

        return {'result': 'invalid data_type, failed'}
        

if __name__ == "__main__":

    app.run(debug=True)