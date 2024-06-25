from threading import Thread, current_thread
import random

import requests

from flask import request
def thd_func():
    numRandom = random.randint(0,1)
    data_type : str
    if numRandom == 0:
        data_type = "temp"
    else:
        data_type = "press"
    
    json = {
        "_id":f"{current_thread().name}",
        "data_type":data_type
    }
    requests.post("http://127.0.0.1:5000/sensor", json = json)

    print(f"[{current_thread().name}] Ho inviato richiesta di registrazione per {data_type}")


    misurazione = {"sensor_id": f"{current_thread().name}"}

    for i in range(5):
        misurazione["data"] = random.randint(1,50)
        requests.post(f"http://127.0.0.1:5000/data/{data_type}", json = misurazione)
    





if __name__ == "__main__":
    NUM_SENSORI = 5
    threadSensori = []

    for i in range(NUM_SENSORI):
        t = Thread(target = thd_func, name = f"S{str(i)}" )
        t.start()
        threadSensori.append(t)
    

    for i in range(len(threadSensori)):
        threadSensori[i].join()



    


        
