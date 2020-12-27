from .utils.helpers import Helpers
import numpy as np
from cv2 import cv2


class Thuggs:

    @staticmethod
    def run(indenification_type):
        Helpers.validate_argument(indenification_type)
        cap = cv2.VideoCapture(0)
        while(True):
            # Capture frame-by-frame
            _ret, frame = cap.read()

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
