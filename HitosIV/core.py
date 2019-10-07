import json
import re
import os

class HitosIV:
    """Una clase para los hitos del proyecto de Infraestructura Virtual"""

    def __init__(self):
        try: # De https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file
            if os.path.exists('hitos.json'):
                path='hitos.json'
            elif os.path.exists('/data/hitos.json'):
                path='/data/hitos.json'
            elif os.path.exists('./data/hitos.json'):
                path='./data/hitos.json'
            elif os.path.exists('../data/hitos.json'):
                path='../data/hitos.json'
            else:
                raise IOError("No se encuentra 'hitos.json'")
                
            with open(path) as data_file:
                self.hitos = json.load(data_file)
        except IOError as fallo:
            print("Error {:s} leyendo hitos.json".format( fallo ) )

    def todos_hitos(self):
        return self.hitos

    def cuantos(self):
        return len(self.hitos['hitos'])

    def uno(self,hito_id):
        if hito_id > len(self.hitos['hitos']) or hito_id < 0:
            raise IndexError("Índice fuera de rango")
        return self.hitos['hitos'][hito_id]

    def nuevo( self, filename, title, fecha ):
        if ( not type(filename) is str):
            raise TypeError( "El nombre del fichero debe ser una cadena" )
        if ( not type(title) is str):
            raise TypeError( "El título del hito debe ser una cadena" )
        if not re.match("\d+/\d+\d+", fecha) :
            raise ValueError( "El formato de la fecha es incorrecto" )
        existe = list(filter( lambda hito: hito['file'] == filename, self.hitos['hitos'] ))
        if len(existe) > 0:
            raise ValueError( "Ese fichero ya existe")
        
        self.hitos['hitos'].append( {'file': filename,
                                     'title': title,
                                     'fecha': fecha } )
