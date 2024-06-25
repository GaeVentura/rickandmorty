
from pymongo import MongoClient
from pymongo import errors
from flask import Flask, request
app = Flask(__name__)

def getDB():
    CONN_STR = "mongodb://127.0.0.1:27017"
    client = MongoClient(CONN_STR)
    return client['sensors']

@app.post("/sensor")
def regSensor():
    regInformation = request.get_json()
    db = getDB()
    sensCollection = db['sensors']
    try:
        sensCollection.insert_one(regInformation)
        return {"result":"success"}
    except errors.DuplicateKeyError:
        print("[CONTROLLER] ERRORE: CHIAVE DUPLICATA")
        return {"result":"failed : DuplicateKeyError"},404

@app.post("/data/<data_type>")
def regMisurazione(data_type):
    misInformation = request.get_json()
    db = getDB()
    collection = db[f"{data_type}"]
    collection.insert_one(misInformation)
    
    return {"result":"success"}



if __name__ == "__main__":

    app.run(debug=True)