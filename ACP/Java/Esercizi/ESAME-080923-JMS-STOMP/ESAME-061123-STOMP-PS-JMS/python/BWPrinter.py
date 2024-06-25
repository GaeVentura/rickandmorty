
import time
import stomp

class BWPrinterListener(stomp.ConnectionListener):

    def __init__(self,conn, file):
        self.conn = conn
        self.file = file

    def on_message(self, frame):
        print(frame.body)
        
        self.file.write(f"{frame.body}\n")



if __name__ == "__main__":
    file = open('bw.txt', mode='w')
    stompConn = stomp.Connection([('127.0.0.1',61613)])

    stompConn.set_listener('', BWPrinterListener(stompConn, file))

    stompConn.connect(wait=True)
    stompConn.subscribe(destination='/queue/bw', id=2, ack='auto')

    time.sleep(5)

    stompConn.disconnect()

    file.close()