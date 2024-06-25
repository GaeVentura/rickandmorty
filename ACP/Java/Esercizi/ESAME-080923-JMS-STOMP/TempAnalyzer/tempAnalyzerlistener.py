import stomp

class tempAnalyzerListener(stomp.ConnectionListener):

    def __init__(self, queue):
        self.queue = queue
    
    def on_message(self, frame):
        print(f"[TEMP-ANALYZER] HO TROVATO: {frame.body}")

