import os
import zlib
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import socket


class UdpSocket:
    def __init__(self):
        self.target_host = "127.0.0.1"
        self.target_port = 8080
        self.udp_socket = None
        '''
        1/2 of 256
        '''
        self.chunk_size = 128
        self.public_key = os.getcwd() + '/../rsa/public_key.pem'

    def get_socket(self):
        if self.udp_socket is None:
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return self.udp_socket

    def send_data(self, data):
        data = self.encrypt_data(data)
        #data = self.encode_data(data)
        print('sending '+str(len(data)))
        data = self.compress_data(data)

        self.get_socket().sendto(data, (self.target_host, self.target_port))
        print(self.get_response())

    '''
    later perhaps we  need to base64 encode/decode
    '''
    def encode_data(self, data):
        data = str.encode(data)
        return data

    def encrypt_data(self, data):
        offset = 0
        encrypted = "".encode()
        fp = open(self.public_key, 'rb')
        rsa_key = RSA.importKey(fp.read().decode())
        oaep_encryptor = PKCS1_OAEP.new(rsa_key)
        fp.close()
        print(len(data))
        while offset < len(data):
            chunk = data[offset:offset + self.chunk_size]
            if len(chunk) % self.chunk_size != 0:
                chunk += " " * (self.chunk_size - len(chunk))
            print('0enc length ' + str(len(chunk)))

            bin_chunk = chunk.encode()
            print('1enc length ' + str(len(bin_chunk)))

            encrypted_chunk = oaep_encryptor.encrypt(bin_chunk)
            print('11enc length ' + str(len(encrypted_chunk)))

            encrypted += encrypted_chunk
            offset += self.chunk_size

        return encrypted

    def compress_data(self, data):
        return zlib.compress(data)

    def decode(self, data):
        return data.decode('utf-8')

    def get_response(self):
        data, addr = self.get_socket().recvfrom(1024)
        return self.decode(data)


client = UdpSocket()

message = "test hjfwejhafb" \
          "jfnewfjkhq"
client.send_data(message)
