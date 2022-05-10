import os
import sys

from pyail import PyAIL

class TemplateFeeder:
    def __init__(self):
        self.FEEDER_UUID = os.getenv('FEEDER_UUID')
        self.FEEDER_NAME = os.getenv('FEEDER_NAME')
        self.FEEDER_ENABLED = os.getenv('FEEDER_ENABLED')
        self.AIL_URL = os.getenv('AIL_URL')
        self.AIL_KEY = os.getenv('AIL_KEY')
        self.AIL_SSLVERIFY = os.getenv('AIL_SSLVERIFY')
        try:
            self.AIL = PyAIL(self.AIL_URL, self.AIL_KEY, ssl=self.AIL_SSLVERIFY)
            print("AIL CONNECTED!\n")
        except Exception as e:
            print(e)
            sys.exit(0)

if __name__ == "__main__":
    Feeder = TemplateFeeder()