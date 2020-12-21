import os
import json

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
        hitos = json.load(data_file)

    hitos['hitos'] = {}
    for h in hitos['hitos_lista']:
        hitos['hitos'][h['file']] = h

except IOError as fallo:
    print("Error {:s} leyendo hitos.json".format( fallo ) )
