import zlib
import socket


class UdpServer:
    def __init__(self):
        self.bind_host = "127.0.0.1"
        self.bind_port = 8080

    def get_socket(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind((self.bind_host, self.bind_port))
        print('listening')
        return self.udp_socket

    def handle_client(self):
        data, addr = self.get_socket().recvfrom(1024)
        print('Received %s ' % str((self.decode(self.decompress(data)), addr)))

    def decode(self, data):
        return data.decode('utf-8')

    def decompress(self,data):
        return zlib.decompress(data)

    def send_data(self, data):
        self.get_socket().sendto(data, self.target_host, self.target_port)


server = UdpServer()
while True:
    server.handle_client()
