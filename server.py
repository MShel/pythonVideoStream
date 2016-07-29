#!/usr/bin/env python
import os
import subprocess

from compression.compressor import Compressor
from transport.server.UdpSocket import UdpSocket

# from encryption.encryptor import Encryptor
from config.config import Config
from queue import Queue
from threading import Thread
from transport import AbstractTransport
import sys
from http.server import *

sys.path.insert(0, os.getcwd())


# Get the args
def main():
    # Clear the screen
    subprocess.call('clear', shell=True)
    config_object = Config(os.getcwd() + '/config/config.ini').raw_config_object
    transport = UdpSocket(config_object)
    image_queue = Queue()

    if config_object['COMPRESSION']['switch'] == 'On':
        compressor = Compressor(config_object)
        transport.add_compression(compressor)

    if config_object['ENCRYPTION']['switch'] == 'On':
        # encryptor = Encryptor(config_object)
        # transport.add_encryption(encryptor)
        print("test")
    try:
        receiver_thread = Thread(target=spin_server, args=(image_queue, transport))
        receiver_thread.start()

        ui_thread = Thread(target=spin_ui_server, args=(image_queue, config_object))
        ui_thread.start()

    except LookupError as e:
        print(e)
        sys.exit(2)

    except KeyboardInterrupt:
        print('keyboard interruption')
        sys.exit(1)


def spin_server(queue: Queue, transport: AbstractTransport):
    while True:
        '''
        do stuff
        '''
        b64image = transport.handle_client()
        queue.put(b64image, False)


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=--jpgboundary')
        self.end_headers()

        while True:
            bin_image = self.queue.get()
            if bin_image is not None:
                self.wfile.write("--jpgboundary".encode())
                self.send_header('Content-type', 'image/jpeg')
                self.send_header('Content-length', str(len(bin_image)))
                self.end_headers()
                self.wfile.write(bin_image)

    def set_queue(self, queue):
        self.queue = queue


def spin_ui_server(image_queue, config_object:dict):
    my_server = HTTPServer((config_object['TRANSPORT']['server_address'], int(config_object['TRANSPORT']['ui_port'])), MyServer)
    my_server.RequestHandlerClass.set_queue(MyServer, image_queue)
    my_server.handle_request()
    my_server.serve_forever()


if __name__ == "__main__":
    main()
