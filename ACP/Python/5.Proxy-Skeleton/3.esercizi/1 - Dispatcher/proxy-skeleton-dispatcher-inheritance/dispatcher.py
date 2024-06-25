from dispatcherImpl import Dispatcher
from multiprocessing import Queue
import sys

NUM_ELEM_QUEUE = 5

if __name__ == '__main__':
    try:
        host = sys.argv[1]
        port = sys.argv[2]
    except IndexError:
        print("Please, specify HOST and/or PORT args")
        sys.exit(-1)

    queue = Queue(NUM_ELEM_QUEUE)
    dispatcher = Dispatcher(host, int(port), queue)
    dispatcher.run_skeleton()
