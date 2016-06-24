
class Client:

    def __init__(self,conf: dict):
        #setup socket
        self.socket = self.setup_socket(conf)

    def send_handshake(self):
        pass

    def initiate_stream(self):
        pass

    def push_stream(self):
        pass

    def encrypt_stream(self):
        pass

    def compress_stream(self):
        pass

    def setup_socket(self,conf:dict):
        #returns socketl
        pass