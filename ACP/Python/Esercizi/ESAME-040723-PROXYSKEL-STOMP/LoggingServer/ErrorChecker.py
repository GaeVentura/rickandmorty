import sys
import time
import stomp

class ErrorCheckerListener(stomp.ConnectionListener):

    def on_message(self, frame):
        print(f"[ERRORCHECKER] HO RICEVUTO {frame.body}")

if __name__ == "__main__":
    try:
        param = sys.argv[1]
    except IndexError:
        print("please, specify msg arg")
    
    stompConn = stomp.Connection([("127.0.0.1", 61613)])

    stompConn.set_listener('', ErrorCheckerListener())

    stompConn.connect(wait=True)
                                                                                                                                                              
    stompConn.subscribe(destination=f"queue/info", id=1, ack='auto')       

    time.sleep(60) 
