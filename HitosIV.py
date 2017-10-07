import json

class HitosIV:
    """Una clase para los hitos del proyecto de Infraestructura Virtual"""

    hitos=[]

    def __init__(self):
        try: # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
            with open('hitos.json') as data_file:
                self.hitos = json.load(data_file)
        except IOError as fallo:
            print("Error %d leyendo hitos.json: %s", fallo.errno,fallo.strerror)
