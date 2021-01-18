import requests
import os
import urllib
from requests import Response
from python_settings import settings


class WebClient:

    def __init__(self, recognition_type):
        self.recognition_type = recognition_type

    def get_trained_data(self):
        """
        Returns XML of Haar Cascade
        """
        if self.recognition_type == 'cat':
            if os.path.exists(f'{os.path.dirname(__file__)}/../data/cat.xml'):
                return
            self.get_cat_haarcascade(self)
        else:
            if os.path.exists(
                f'{os.path.dirname(__file__)}/../data/deploy.prototxt') and os.path.exists(
                    f'{os.path.dirname(__file__)}/../data/bvlc_googlenet.caffemodel'):
                return

            if not os.path.exists(f'{os.path.dirname(__file__)}/../data/deploy.prototxt'):
                self.get_prototxt_file(self)
            if not os.path.exists(f'{os.path.dirname(__file__)}/../data/bvlc_googlenet.caffemodel'):
                self.get_caffe_data(self)
            return

    @staticmethod
    def get_cat_haarcascade(self):
        """
        Get haarcascade file for cat identification
        """
        response = requests.get(
            f'{settings.HAARCASCADE_URL}/haarcascade_frontalcatface.xml',
            timeout=40)
        if response.status_code != 200:
            Response.raise_for_status(response)

        self.haarcascade_tmp_file(response.text, self.recognition_type)
        return

    @staticmethod
    def haarcascade_tmp_file(cascade_data, recognition_type):
        """
        Save cat haarcascade file
        """
        file = open(f'{os.path.dirname(__file__)}/../data/{recognition_type}.xml', 'w')
        file.write(cascade_data)
        file.close()
        return

    @staticmethod
    def get_caffe_data(self):
        """
        Downloads caffe model data
        """
        params = {'timeout': 40, 'stream': True}
        response = requests.get(settings.CAFFEMODEL_URL, params)
        totalbits = 0
        if response.status_code != 200:
            Response.raise_for_status(response)
        with open(f'{os.path.dirname(__file__)}/../data/bvlc_googlenet.caffemodel', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    totalbits += 1024
                    print('Model downloaded', totalbits * 1025, "KB...")
                    f.write(chunk)

    @staticmethod
    def get_prototxt_file(self):
        """
        Save caffe model
        """
        response = requests.get(settings.PROTOTXT_URL, timeout=40)
        if response.status_code != 200:
            Response.raise_for_status(response)

        file = open(f'{os.path.dirname(__file__)}/../data/deploy.prototxt', 'w')
        file.write(response.text)
        file.close()
        return
