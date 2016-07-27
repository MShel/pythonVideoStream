from compression.compressor import Compressor
#from encryption.encryptor import Encryptor


class AbstractTransport:
    def __init__(self):
        self.compressor = None
        self.encryptor = None

    def encrypt_data(self, data):
        try:
            result = data.encode()
        except AttributeError:
            # got binary already
            result = data

        if self.encryptor is not None:
            result = self.encryptor.encrypt(data)
        return result

    def decrypt_data(self, data):
        result = data
        if self.encryptor is not None:
            result = self.encryptor.decrypt(data)
        return result

    def compress_data(self, data):
        result = data
        if self.compressor is not None:
            result = self.compressor.compress(data)
        return result

    def uncompress_data(self, data):
        result = data
        print(data)
        if self.compressor is not None:
            result = self.compressor.uncompress(data)
        print('test')
        print(data)
        return result

    def add_compression(self, compressor: Compressor):
        self.compressor = compressor

    #def add_encryption(self, encryptor: Encryptor):
    #    self.encryptor = encryptor
