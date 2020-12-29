import thuggs.exceptions.exceptions as exceptions
from thuggs.classes.recognizer import Recognizer
import thuggs
import sys
import os
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))
