import socket


class UdpSocket:
    def __init__(self):
        self.target_host = "127.0.0.1"
        self.target_port = 8080

    def get_socket(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return self.udp_socket

    def send_data(self, data):
        self.get_socket().sendto(data, (self.target_host, self.target_port))

    def get_response(self):
        data, addr = self.get_socket().recvfrom(4096)
        return data, addr


client = UdpSocket()
message = "test"
client.send_data(str.encode(message))
print(client.get_response())
