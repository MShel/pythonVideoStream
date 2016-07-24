import base64
import os

from cv2 import *


class Camera:
    MAX_PHOTO_FAILURE_ATTEMPTS = 5

    def __init__(self, config_obj: dict):
        self.camera = VideoCapture(0)
        self.config = config_obj
        self.failure_counter = 0

    def get_frame(self):
        rc, img = self.camera.read()
        if rc:
            imwrite(self.config['FILES']['buffer_file'], img)
            self.failure_counter = 0
            with open(self.config['FILES']['buffer_file'], 'rb') as content_file:
                img = content_file.read()
            os.remove(self.config['FILES']['buffer_file'])
            return base64.b64encode(img)
        else:
            # trying again
            if self.failure_counter < self.MAX_PHOTO_FAILURE_ATTEMPTS:
                self.failure_counter += 1
                self.get_frame()

    def get_test_image(self):
        with open(os.getcwd() + '/camera/test.jpeg', 'rb') as test_img:
            test = test_img.read()
        return base64.b64encode(test)
