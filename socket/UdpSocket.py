import socket
import zlib


class UdpSocket:
    def __init__(self):
        self.target_host = "127.0.0.1"
        self.target_port = 8080

    def get_socket(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return self.udp_socket

    def send_data(self, data):
        data = self.compress_data(self.encode_data(data))
        self.get_socket().sendto(data, (self.target_host, self.target_port))

    def encode_data(self,data):
        data = str.encode(data)
        return data

    def compress_data(self, data):
        return zlib.compress(data)


client = UdpSocket()
message = "test hjfwejhafb" \
          "jfnewfjkhq"
client.send_data(message)
print(client.get_response())
