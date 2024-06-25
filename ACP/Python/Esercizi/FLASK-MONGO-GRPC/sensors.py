

import random
from threading import Thread, get_ident, current_thread

import requests

def thd_func(dataType):

    print(current_thread().name)


    jsonReq = {
        '_id': f"{current_thread().name}",
        'data_type' : dataType
    }
    backMessage = requests.post('http://127.0.0.1:5000/sensor', json = jsonReq)

    print(backMessage.json())


    for i in range(5):
        sensMis = {
            'sensor_id': f"{current_thread().name}",
            'data' : random.randint(1,50)
        }

        requests.post(f'http://127.0.0.1:5000/data/<{dataType}>', json = sensMis)

if __name__ == "__main__":

    N_THREADS = 5

    for i in range(N_THREADS):
        casual = random.randint(0,1)

        if casual == 0 :
            dataType = 'temp'
        else :
            dataType = 'press'
        t = Thread(target = thd_func, name = f"S{str(i)}",  args = (dataType,) )

        t.start()

    
