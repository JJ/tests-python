"""Hitos de IV servidos para usted"""

import os
import logging

import hug
from hug.middleware import LogMiddleware

from pythonjsonlogger import jsonlogger

from datetime import datetime

from HitosIV import HitosIV

""" Define logger en JSON """
class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger()
        logHandler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter()
        logHandler.setFormatter(formatter)
        self.logger.addHandler(logHandler)

    def process_request(self, request, response):
        """Logs the basic endpoint requested"""
        self.logger.info({ 'method': request.method,
                           'uri': request.relative_uri,
                           'type': request.content_type } )

    def process_response(self, request, response, resource):
        """Logs the basic data returned by the API"""
        current_time = datetime.utcnow()
        self.logger.info( {'remote_addr':request.remote_addr,
                           't': current_time,
                           'method': request.method,
                           'uri': request.relative_uri,
                           'status': response.status,
                           'user-agent': request.user_agent })
        
    def info(self, content):
        self.logger.info( content )

        

@hug.middleware_class()
class CustomLogger(LogMiddleware):
    def __init__(self, logger=Logger()):
        super().__init__(logger=logger)

""" Declara clase """ 
estos_hitos = HitosIV()

""" Define API """ 
@hug.get('/')
def status():
    """Devuelve estado"""
    return { "status": "OK" }

@hug.get('/status')
def status():
    """Devuelve estado"""
    return { "status": "OK" }

@hug.get('/all')
def all():
    """Devuelve todos los hitos"""
    return { "hitos": estos_hitos.todos_hitos() }

@hug.get('/one/{id}')
def one( id: int ):
    """Devuelve un hito"""
    return { "hito": estos_hitos.uno( id ) }

if 'PORT' in os.environ :
    port = int(os.environ['PORT'])
else:
    port = 8000

if __name__ == '__main__':
    hug.API(__name__).http.serve(port )
