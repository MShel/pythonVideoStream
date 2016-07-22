import socket

from transport.AbstractTransport import AbstractTransport


class UdpSocket(AbstractTransport):
    def __init__(self, config: dict):
        AbstractTransport.__init__(self)
        self.bind_host = config['TRANSPORT']['server_address']
        self.bind_port = int(config['TRANSPORT']['port'])
        self.udp_socket = None

    def get_socket(self):
        if self.udp_socket is None:
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_socket.bind((self.bind_host, self.bind_port))
        return self.udp_socket

    def handle_client(self):
        data, addr = self.get_socket().recvfrom(49152)
        decompressed = self.uncompress_data(data)
        data = self.decrypt_data(decompressed)
        print('len7' + str(len(data)))
        print('\n' + data + '\n')
        print('Received %s ' % str((data, addr)))
        self.get_socket().sendto('got it'.encode(), addr)
