import json

class HitosIV:
    """Una clase para los hitos del proyecto de Infraestructura Virtual"""

    def __init__(self):
        try: # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
            with open('hitos.json') as data_file:
                self.hitos = json.load(data_file)
        except IOError as fallo:
            print("Error %d leyendo hitos.json: %s", fallo.errno,fallo.strerror)

    def todos_hitos(self):
        return self.hitos

    def cuantos(self):
        return len(self.hitos['hitos'])

    def uno(self,hito_id):
        if hito_id > len(self.hitos['hitos']) or hito_id < 0:
            raise IndexError("Índice fuera de rango")
        return self.hitos['hitos'][hito_id]
