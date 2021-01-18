import os
import numpy as np
from cv2 import cv2
from ..exceptions.exceptions import IllegalArgumentError
from .web_client import WebClient

class Recognizer:

    def __init__(self, recognition_type):
        self.recognition_type = recognition_type

    @property
    def recognition_type(self):
        """
        Returns recogizer type attribute
        """
        return self._recognition_type

    @recognition_type.setter
    def recognition_type(self, value):
        """
        Sets recogizer type attribute and validates it
        """
        if(value == 'cat' or value == 'human'):
            self._recognition_type = value
            return

        raise IllegalArgumentError('Must use "cat" or "human" for argument.')

    def setup_data(self):
        """
        Retrieves and stores cascades or DNN model from GitHub if they do not already exist
        """
        WebClient(self.recognition_type).get_trained_data()

        return


    def get_grayscale(self):
        """
        Returns greyscale version of frame
        """
        pass