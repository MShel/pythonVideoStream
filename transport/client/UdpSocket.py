import socket

from transport.AbstractTransport import AbstractTransport


class UdpSocket(AbstractTransport):
    def __init__(self, config: dict):
        AbstractTransport.__init__(self)
        self.target_host = config['TRANSPORT']['server_address']
        self.target_port = int(config['TRANSPORT']['port'])
        self.udp_socket = None
        self.buffer = self.get_socket().getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)

    def get_socket(self) -> socket:
        if self.udp_socket is None:
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return self.udp_socket

    def send_data(self, data):
        data = self.encrypt_data(data)
        print('sending ' + str(len(data)))
        data = self.compress_data(data)
        print('compressed ' + str(len(data)))
        self.send_sentinel_start()
        self.send_chunked_data(data)
        self.send_sentinel_end()
        print(self.get_response())

    def get_response(self):
        data, addr = self.get_socket().recvfrom(1024)
        return data.decode('utf-8')

    def send_chunked_data(self, data):
        try:
            offset = 0
            while offset < len(data):
                chunk = data[offset:offset + self.buffer]
                if len(chunk) % self.buffer != 0:
                    try:
                        chunk += " " * (self.buffer - len(chunk))
                    except TypeError:
                        chunk += " ".encode() * (self.buffer - len(chunk))
                try:
                    bin_chunk = chunk.encode()
                except AttributeError:
                    bin_chunk = chunk

                offset += self.buffer
                self.get_socket().sendto(bin_chunk, (self.target_host, self.target_port))
        except OSError:
            self.buffer -= 1024
            self.send_chunked_data(data)

        print('Sent!')

    def send_sentinel_start(self):
        self.get_socket().sendto('message start'.encode(), (self.target_host, self.target_port))

    def send_sentinel_end(self):
        self.get_socket().sendto('message end'.encode(), (self.target_host, self.target_port))
