import cv2
import numpy as np
import unittest
from autocrop import crop

class TestCrop(unittest.TestCase):
    def test_smoke(self):
        crop('tests/test_image.jpg')
        return
    
    def test_oneshot(self):
        with self.assertRaises(AssertionError):
            crop(1)
        return
    
    def test_oneshot1(self):
        with self.assertRaises(AssertionError):
            crop()
        return
    
