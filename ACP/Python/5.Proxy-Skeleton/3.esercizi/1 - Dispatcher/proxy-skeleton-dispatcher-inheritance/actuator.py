import sys
import threading as mt
import random
from datetime import datetime
from dispatcherProxy import DispatcherProxy      


if __name__ == "__main__":

    try:
        HOST = sys.argv[1]
        PORT = sys.argv[2]
    except IndexError:
        print("Please, specify HOST/PORT args...")
        sys.exit(-1)

    cmd_dict = {0:"leggi", 1:"scrivi", 2:"configura", 3:"reset"}    
    i = 0
    
    while True:
        proxy = DispatcherProxy(HOST, int(PORT), mt.current_thread().name)
        data = proxy.getCmd()

        print(f'[ACTUATOR] received data for #{i} request: {data}...write to file\n')
        
        with open("cmdLog.txt", mode="a") as cmdlog_file:
            cmdlog_file.write(f'{datetime.now()} {cmd_dict[int(data)]}\n')
        
        i = i + 1