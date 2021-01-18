"""Hitos de IV servidos para usted"""

import os
import logging

import hug
from hug.middleware import LogMiddleware
from logstash_async.handler import AsynchronousLogstashHandler
from datetime import datetime

from HitosIV.core import HitosIV

""" Define logger en JSON 

Recordar definir la configuración de logstash así:

    export LOGSTASH_CONF_STRING='input {      tcp {     port => 8080     codec => json   } } output { stdout {} }'

En este caso, para el contenedor de Docker de Bitnami
"""
@hug.middleware_class()
class CustomLogger(LogMiddleware):
    def __init__(self):
        host = 'localhost'
        logger = logging.getLogger('python-logstash-logger')
        logger.setLevel(logging.INFO)
        logger.addHandler(AsynchronousLogstashHandler(host, 8080, database_path=''))
        super().__init__(logger=logger)

    def _generate_combined_log(self, request, response):
        """Genera un formato parecido a nginx"""
        return {'remote_addr':request.remote_addr,
                'time': datetime.utcnow().strftime('%B %d %Y - %H:%M:%S'),
                'method': request.method,
                'uri': request.relative_uri,
                'status': response.status,
                'user-agent': request.user_agent }


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

api = hug.API(__name__)

if __name__ == '__main__':
    hug.API(__name__).http.serve( port )
