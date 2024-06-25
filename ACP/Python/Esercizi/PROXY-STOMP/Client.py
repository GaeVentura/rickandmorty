from random import randint
import time
import stomp

class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_message(self, frame):
        print(f"[CLIENT] HO RICEVUTO MSG: {frame.body}")


if __name__ == "__main__":
    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait = True)
    N = 10
    for i in range(N):
        casual = randint(0,1)
        id = randint(0,3)
        if i < 5:
            MSG = "deposita"+"-"+str(id)
            conn.send('queue/es2_Richiesta', MSG)
            print(f"[CLIENT] INVIO MSG: {MSG}")
        else:
            MSG = "preleva"+"-"+str(id)
            conn.send('queue/es2_Richiesta', MSG)
            print(f"[CLIENT] INVIO MSG: {MSG}") 
                       

    conn.set_listener('',MyListener(conn))

    conn.subscribe(destination="queue/es2_Risposta", id = 2, ack='auto')

    
    print("[LISTENER] Attendo MSG")

    time.sleep(50)
