import requests
import os
import urllib
from requests import Response
from python_settings import settings


class WebClient:

    def __init__(self, recognition_type):
        self.recognition_type = recognition_type

    def get_trained_data(self, paths):
        """
        Returns XML of Haar Cascade
        """
        if self.recognition_type == 'cat':
            if os.path.exists(paths['cascades_path']):
                return
            self.get_cat_haarcascade(self, paths)
        else:
            if os.path.exists(paths['prototxt_path']) and os.path.exists(paths['model_path']):
                return

            if not os.path.exists(paths['prototxt_path']):
                self.get_prototxt_file(self, paths)
            if not os.path.exists(paths['model_path']):
                self.get_caffe_data(self, paths)
            return

    @staticmethod
    def get_cat_haarcascade(self, paths):
        """
        Get haarcascade file for cat identification
        """
        response = requests.get(
            f'{settings.HAARCASCADE_URL}/haarcascade_frontalcatface.xml',
            timeout=40)
        if response.status_code != 200:
            Response.raise_for_status(response)

        self.haarcascade_tmp_file(response.text, paths)
        return

    @staticmethod
    def haarcascade_tmp_file(cascade_data, paths):
        """
        Save cat haarcascade file
        """
        file = open(paths['cascades_path'], 'w')
        file.write(cascade_data)
        file.close()
        return

    @staticmethod
    def get_caffe_data(self, paths):
        """
        Downloads caffe model data
        """
        params = {'timeout': 40, 'stream': True}
        response = requests.get(settings.CAFFEMODEL_URL, params)
        totalbits = 0
        if response.status_code != 200:
            Response.raise_for_status(response)
        with open(paths['model_path'], 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    totalbits += 1024
                    print('Model downloaded', totalbits * 1025, "KB...")
                    f.write(chunk)

    @staticmethod
    def get_prototxt_file(self, paths):
        """
        Save caffe model
        """
        response = requests.get(settings.PROTOTXT_URL, timeout=40)
        if response.status_code != 200:
            Response.raise_for_status(response)

        file = open(paths['prototxt_path'], 'w')
        file.write(response.text)
        file.close()
        return
