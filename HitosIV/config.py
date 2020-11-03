import etcd3
from dotenv import load_dotenv
import os
import sys


class Config:

    def __init__(self):
        PORT_VAR_NAME= 'hugitos:PORT'
        try: 
            etcd = etcd3.client()
            self.port = int(etcd.get(PORT_VAR_NAME)[0].decode("utf8") )
        except:
            load_dotenv()
            if (os.getenv('PORT')):
                self.port = os.getenv('PORT')
            else:
                self.port = 3000
