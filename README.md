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
* pip install -r requirements.txt
* adjust config.ini
* on the server python server.py
* on the client python client.py

## Trello board with info of what is going on:
https://trello.com/b/ZxRjPN2B/pythonvideostream