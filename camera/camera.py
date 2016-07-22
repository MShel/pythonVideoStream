import base64
import os
#from cv2 import *


class Camera:
    def __init__(self, config_obj: dict):
        #self.camera = VideoCapture(0)
        self.config = config_obj

    def get_image(self):
        rc, img = self.camera.read()
        if rc:
            imwrite('/tmp/buffer.jpg', img)
            with open('/tmp/buffer.jpg', 'rb') as content_file:
                img = content_file.read()
            os.remove('/tmp/buffer.jpg')
            return base64.b64encode(img)
        else:
            raise Error()

    def get_test_image(self):
        with open(os.getcwd()+'/camera/test.jpeg','rb') as test_img:
            test = test_img.read()
        return base64.b64encode(test)
