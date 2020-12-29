import os
from ..exceptions.exceptions import IllegalArgumentError

class Recognizer:

    def __init__(self, recognition_type):
        self.recognition_type = recognition_type

    @property
    def recognition_type(self):
        """
        docstring
        """
        return self._recognition_type

    @recognition_type.setter
    def recognition_type(self, value):
        """
        docstring
        """
        if(value == 'cat' or value == 'human'):
            self._recognition_type = value
            return

        raise IllegalArgumentError('Must use "cat" or "human" for argument.')
