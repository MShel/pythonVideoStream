class Server:
    def __init__(self, conf: dict):
        # setup socket
        self.socket = self.setup_socket(conf)

    def accept_handshake(self):
        pass

    def get_stream(self):
        pass

    def decrypt_stream(self):
        pass

    def decompress_stream(self):
        pass

    def setup_socket(self, conf: dict):
        # returns socket
        pass
