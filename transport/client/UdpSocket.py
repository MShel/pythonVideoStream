import socket
import zlib

from transport.AbstractTransport import AbstractTransport


class UdpSocket(AbstractTransport):
    def __init__(self, config: dict):
        AbstractTransport.__init__(self)
        self.target_host = config['TRANSPORT']['server_address']
        self.target_port = int(config['TRANSPORT']['port'])
        self.udp_socket = None

    def get_socket(self):
        if self.udp_socket is None:
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return self.udp_socket

    def send_data(self, data):
        data = self.encrypt_data(data)
        print('sending ' + str(len(data)))
        data = self.compress_data(data)
        self.get_socket().sendto(data, (self.target_host, self.target_port))
        print(self.get_response())

    def get_response(self):
        data, addr = self.get_socket().recvfrom(1024)
        return data.decode('utf-8')