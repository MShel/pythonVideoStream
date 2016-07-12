#!/usr/bin/env python
import os
import subprocess
import sys

from config.config import Config
from compression.compressor import Compressor
from transport.client.UdpSocket import UdpSocket
from encryption.encryptor import Encryptor
from pprint import pprint

sys.path.insert(0, os.getcwd())


# Get the args
def main():
    # Clear the screen
    subprocess.call('clear', shell=True)
    config_object = Config(os.getcwd() + '/config/config.ini').raw_config_object
    transport = UdpSocket(config_object)

    if config_object['COMPRESSION']['switch'] == 'On':
        compressor = Compressor(config_object)
        transport.add_compression(compressor)

    if config_object['ENCRYPTION']['switch'] == 'On':
        encryptor = Encryptor(config_object)
        transport.add_encryption(encryptor)


    try:
        transport.send_data("ATATA")

    except LookupError as e:
        print(e)
        sys.exit(2)

    except KeyboardInterrupt:
        print('keyboard interruption')
        sys.exit(1)


if __name__ == "__main__":
    main()