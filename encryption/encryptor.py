import os

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


class Encryptor:

    def __init__(self, config: dict):
        self.public_key_path = os.getcwd() + '/encryption/rsa/public_key.pem'
        self.private_key_path = os.getcwd() + '/encryption/rsa/private_key.pem'
        self.chunk_size = 128

    def encrypt(self, data):
        offset = 0
        encrypted = "".encode()
        fp = open(self.public_key_path, 'rb')
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

    def decrypt(self,data):
        print('\n ...decrypting... \n')
        priv_key_file = open(self.private_key_path, 'rb')
        rsa_key = RSA.importKey(priv_key_file.read().decode())
        decryptor = PKCS1_OAEP.new(rsa_key)
        priv_key_file.close()
        decrypted = decryptor.decrypt(data).decode()
        return decrypted
