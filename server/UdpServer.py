import threading

import socket


class UdpServer:
    def __init__(self):
        self.bind_host = "127.0.0.1"
        self.bind_port = 8080

    def get_socket(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.udp_socket.bind((self.bind_host, self.bind_port))
        self.udp_socket.listen(5)
        print('listening')
        return self.udp_socket

    def handle_client(self, client_socket: socket):
        request = client_socket.recv(1024)
        print("Received %s" % request)
        client_socket.send('done')
        client_socket.close()

    def send_data(self, data):
        self.get_socket().sendto(data, self.target_host, self.target_port)

    def get_response(self):
        data, addr = self.get_socket().recvfrom(4096)
        return data, addr


server = UdpServer()

while True:
    client, add = server.get_socket().accept()
    client_handler = threading.Thread(target=server.handle_client, args=(client,))
    client_handler.start()
