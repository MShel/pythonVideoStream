import os
import zlib

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import socket


class UdpServer:
    def __init__(self):
        self.bind_host = "127.0.0.1"
        self.bind_port = 8080
        self.chunk_size = 256
        self.udp_socket = None
        self.private_key = os.getcwd() + '/rsa/private_key.pem'

    def get_socket(self):
        if self.udp_socket is None:
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_socket.bind((self.bind_host, self.bind_port))

        return self.udp_socket

    def handle_client(self):
        print('\n ...receiving... \n')
        data, addr = self.get_socket().recvfrom(1024)
        decompressed = self.decompress(data)
        data = self.decrypt(decompressed)
        print('len7'+str(len(data)))
        print('\n'+ data +'\n')
        print('Received %s ' % str((data, addr)))
        self.get_socket().sendto('got it'.encode(), addr)

    def decrypt(self, data):
        print('\n ...decrypting... \n')
        priv_key_file = open(self.private_key, 'rb')
        rsa_key = RSA.importKey(priv_key_file.read().decode())
        decryptor = PKCS1_OAEP.new(rsa_key)
        priv_key_file.close()
        decrypted = decryptor.decrypt(data).decode()

        return decrypted

    '''
    later perhaps we  need to base64 encode/decode
    '''

    def decode(self, data):
        return data.decode('utf-8')

    def decompress(self, data):
        return zlib.decompress(data)

    def send_data(self, data):
        self.get_socket().sendto(data, self.target_host, self.target_port)


server = UdpServer()

while True:
    server.handle_client()
