import zlib


class Compressor:
    def __init__(self, config: dict):
        self.encryptionType = 'zlib'

    def compress(self, data):
        return zlib.compress(data)

    def uncompress(self, data):
        return zlib.decompress(data)
