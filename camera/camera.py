import base64
import io
import math
import os
from cv2 import *

from PIL import Image
from PIL import ImageChops


class Camera:
    MAX_PHOTO_FAILURE_ATTEMPTS = 5

    def __init__(self, config_obj: dict):
        self.camera = VideoCapture(0)
        self.config = config_obj
        self.failure_counter = 0
        self.prev_image = None

    def get_frame(self):
        rc, img = self.camera.read()
        if rc:
            pil_image = Image.fromarray(img)
            if self.prev_image is None or self.compare_images(pil_image) > float(self.config['QUALITY']['similarity_coeff']):
                output = io.BytesIO()
                self.prev_image = pil_image
                pil_image.save(output, format='JPEG')
                return output.getvalue()
            else:
                self.get_frame()
        else:
            # trying again
            if self.failure_counter < self.MAX_PHOTO_FAILURE_ATTEMPTS:
                self.failure_counter += 1
                self.get_frame()

    def compare_images(self, curr_image: Image) -> float:
        diff = ImageChops.difference(curr_image, self.prev_image)
        h = diff.histogram()
        sq = (value * (idx ** 2) for idx, value in enumerate(h))
        sum_of_squares = sum(sq)
        rms = math.sqrt(sum_of_squares / float(curr_image.size[0] * self.prev_image.size[1]))
        return rms

    def get_test_image(self):
        with open(os.getcwd() + '/camera/test.jpeg', 'rb') as test_img:
            test = test_img.read()
        return base64.b64encode(test)
