from queue import Queue
import time
import stomp
from tempAnalyzerlistener import tempAnalyzerListener

if __name__ == "__main__":
    stompConn = stomp.Connection([('127.0.0.1', 61613)])
    stompConn.connect(wait = True)
    queue = Queue()
    stompConn.set_listener('', tempAnalyzerListener(queue))
    stompConn.subscribe("/topic/temp", id = 1 )

    time.sleep(60)

    stompConn.disconnect()

    