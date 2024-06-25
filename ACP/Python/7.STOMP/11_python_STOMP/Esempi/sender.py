import sys, stomp
    

if __name__ == "__main__":

    try:
            MSG = sys.argv[1]
    except IndexError:
            print("Please, specify MSG arg")

    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait=True)

    conn.send('/queue/test', MSG)
    #conn.send('/topic/mytesttopic', MSG) 

    print("Message: -", MSG, "- sent")

    conn.disconnect()
