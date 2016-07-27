import base64
import os
from cv2 import *
import io
from PIL import Image


class Camera:
    MAX_PHOTO_FAILURE_ATTEMPTS = 5

    def __init__(self, config_obj: dict):
        self.camera = VideoCapture(0)
        self.config = config_obj
        self.failure_counter = 0

    def get_frame(self):
        rc, img = self.camera.read()
        if rc:
            pil_image = Image.fromarray(img)
            output = io.BytesIO()
            pil_image.save(output, format='JPEG')
            return base64.b64encode(output.getvalue())
        else:
            # trying again
            if self.failure_counter < self.MAX_PHOTO_FAILURE_ATTEMPTS:
                self.failure_counter += 1
                self.get_frame()
            # TODO need to add else raise Error(photo taking failed... and camera close)
    def get_test_image(self):
        with open(os.getcwd() + '/camera/test.jpeg', 'rb') as test_img:
            test = test_img.read()
        return base64.b64encode(test)
