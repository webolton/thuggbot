import requests, os
from requests import Response
from python_settings import settings

class WebClient:

    def __init__(self, recognition_type):
        self.recognition_type = recognition_type

    def get_cascade(self):
        """
        Returns XML of Haar Cascade
        """
        if os.path.exists(f'{os.path.dirname(__file__)}/../data/{self.recognition_type}.xml'):
            return

        response = requests.get(f'{settings.HAARCASCADE_URL}/{self.cascade_filename()}', timeout=40)
        if response.status_code != 200:
            Response.raise_for_status(response)

        self.haarcascade_tmp_file(response.text, self.recognition_type)
        return

    @staticmethod
    def haarcascade_tmp_file(cascade_data, recognition_type):
        """
        docstring
        """
        file = open(f'{os.path.dirname(__file__)}/../data/{recognition_type}.xml', 'w')
        file.write(cascade_data)
        file.close()
        return

    def cascade_filename(self):
        """
        Returns filename based on recognition_type
        """
        if self.recognition_type == 'cat':
            return 'haarcascade_frontalcatface.xml'
        return 'haarcascade_frontalface_alt2.xml'
