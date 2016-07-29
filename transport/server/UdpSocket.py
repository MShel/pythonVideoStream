import socket

from transport.AbstractTransport import AbstractTransport


class UdpSocket(AbstractTransport):
    def __init__(self, config: dict):
        AbstractTransport.__init__(self)
        self.bind_host = config['TRANSPORT']['server_address']
        self.bind_port = int(config['TRANSPORT']['port'])
        self.udp_socket = None
        self.result_file = None

    def get_socket(self):
        if self.udp_socket is None:
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_socket.bind((self.bind_host, self.bind_port))
        return self.udp_socket

    def handle_client(self):
        buffer = self.get_socket().getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        data, addr = self.get_socket().recvfrom(buffer)
        try:
            sentinel_start = data.decode()
        except UnicodeDecodeError:
            sentinel_start = None

        if self.result_file is None or sentinel_start == "message start":
            self.result_file = ''.encode()
        else:

            try:
                sentinel_end = data.decode()
                if sentinel_end == "message end":
                    return self.return_received(addr)
                else:
                    self.result_file += data
            except (UnicodeDecodeError):
                self.result_file += data
            except AttributeError:
                self.result_file += data.encode()

    def return_received(self, addr):
        decompressed = self.uncompress_data(self.result_file)
        self.get_socket().sendto('got it'.encode(), addr)
        return decompressed
