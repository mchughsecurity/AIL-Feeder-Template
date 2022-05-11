import os
import sys
import redis
import logging
from pyail import PyAIL


class TemplateFeeder:
    def __init__(self):
        self.FEEDER_UUID = os.getenv('FEEDER_UUID')
        self.FEEDER_NAME = os.getenv('FEEDER_NAME')
        self.FEEDER_ENABLED = os.getenv('FEEDER_ENABLED')

        self.AIL_URL = os.getenv('AIL_URL')
        self.AIL_KEY = os.getenv('AIL_KEY')
        self.AIL_SSLVERIFY = os.getenv('AIL_SSLVERIFY')

        self.REDIS_HOST = os.getenv('REDIS_HOST')
        self.REDIS_PORT = os.getenv('REDIS_PORT')
        self.REDIS_DB = os.getenv('REDIS_DB')
        self.REDIS = redis.Redis(host=self.REDIS_HOST,port=self.REDIS_PORT,db=self.REDIS_DB)

        try:

            logging.info("Creating test payload...\n")
            test_payload = 'Test string being submitted to AIL via PyAIL';
            test_payload_meta = {}
            test_payload_meta['some_attribute'] = 'some value'

            logging.info("Testing connection to AIL...\n")
            self.PYAIL = PyAIL(self.AIL_URL, self.AIL_KEY, ssl=False)

            logging.info("Sending TEST payload {} with API Key {}. SSL Verify {}.\n".format(self.AIL_URL, self.AIL_KEY,
                                                                                            self.AIL_SSLVERIFY))

            # Send the test payload to AIL
            self.send_to_ail(data=test_payload,meta=test_payload_meta)

        except Exception as e:
            print(e)
            sys.exit(0)

    def construct_item_text(self,type,tags,text):
        ail_data = {
            'type': type,
            'tags': tags,
            'text': text
        }
        return ail_data

    def send_to_ail(self,data,meta):
        try:
            response = self.PYAIL.feed_json_item(
                data=data,
                meta=meta,
                source=self.FEEDER_NAME,
                source_uuid=self.FEEDER_UUID
            )
            logging.info("Packet has been sent to AIL\n")
        except Exception as e:
            print(e)
            sys.exit(0)

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s:%(message)s', level=logging.INFO, datefmt='%I:%M:%S')
    Feeder = TemplateFeeder()