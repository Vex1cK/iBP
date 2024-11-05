import logging
logger = logging.getLogger(__name__)

import requests
from PySide6.QtCore import QRunnable
from src.config.config import get_current_token

class MLClient(QRunnable):
    def __init__(self, url, input_file_path, output_file_path, callback):
        super().__init__()
        self.url = url
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.callback = callback
        self.params = {"access_token": get_current_token()}
        logger.debug("MLClient initialized")

    def run(self):
        logger.debug("MLClient started")
        try:
            with open(self.input_file_path, 'rb') as file:
                logger.debug(f"Sending file {self.input_file_path}")
                response = requests.post(self.url, files={"file": file}, params=self.params)
                logger.debug(f"Response: {response.status_code}")
            
            if response.status_code != 200:
                self.callback(False, response.detail)
                return

            with open(self.output_file_path, "w") as file:
                file.write(response.text)

            self.callback(True, 'Ok')
            logger.debug("MLClient finished")
        except Exception as e:
            self.callback(False, str(e))
