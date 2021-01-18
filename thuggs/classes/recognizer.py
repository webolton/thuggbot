import os
import numpy as np
from cv2 import cv2
from ..exceptions.exceptions import IllegalArgumentError
from .web_client import WebClient


class Recognizer:

    def __init__(self, recognition_type):
        self.recognition_type = recognition_type
        self.recognizer_paths = {}

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

    @property
    def recognizer_paths(self):
        """
        Returns recogizer type attribute
        """
        return self._recognizer_paths

    @recognizer_paths.setter
    def recognizer_paths(self, value):
        """
        Sets recogizer type attribute and validates it
        """
        if self.recognition_type == 'cat':
            self._recognizer_paths = {
                'cascade_path': f'{os.path.dirname(__file__)}/../data/cat.xml'
            }
            return
        if self.recognition_type == 'human':
            self._recognizer_paths = {
                'prototxt_path': f'{os.path.dirname(__file__)}/../data/deploy.prototxt',
                'model_path': f'{os.path.dirname(__file__)}/../data/bvlc_googlenet.caffemodel'
            }
            return

    def setup_data(self):
        """
        Retrieves and stores cascades or DNN model from GitHub if they do not already exist
        """
        WebClient(self.recognition_type).get_trained_data(self.recognizer_paths)
        return

    def cat_cascades(self):
        """
        Returns cat face cascades
        """
        cascades = cv2.CascadeClassifier(self.recognizer_paths['cascade_path'])
        return cascades

    def human_net(self):
        """
        Returns neural net for recognizing human faces
        """
        # net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])
        return cv2.dnn.readNetFromCaffe(
            self.recognizer_paths['prototxt_path'], self.recognizer_paths['model_path']
            )

    def get_grayscale(self):
        """
        Returns greyscale version of frame
        """
        pass
