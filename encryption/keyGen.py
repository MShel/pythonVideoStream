from Crypto.PublicKey import RSA


class KeyGen:
    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.folder_store = './'

    def generate_pair(self):
        new_key = RSA.generate(2048, e=65537)
        public_key = new_key.publickey().exportKey("PEM").decode('utf-8')
        private_key = new_key.exportKey("PEM").decode('utf-8')
        with open('public_key.pem', 'w+') as f:
            f.write(public_key)
        with open('private_key.pem', 'w+') as f:
            f.write(private_key)

keyGenerator = KeyGen()
keyGenerator.generate_pair()