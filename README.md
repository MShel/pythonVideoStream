# pythonVideoStream

Client will generate MJPEG stream and based on config/config.ini
It will be pushed in different forms to server:
* not encrypted, not compressed
* encrypted, compressed
* encrypted or compressed

Server will serve mjpeg on ui_port available to view through web interface

To enable encryption you need to run keyGen.py to generate priv/public keys
Also make sure that switches are on in config.ini

##How to run:
* sudo python3 client.py (on the client side (where the camera is))
* sudo python3 server.py (on the server side (where the web ui should be))

## Things you need to run it
* linux
* python3
* openCv
* python Crypto (sudo apt-get install python3-crypto)

