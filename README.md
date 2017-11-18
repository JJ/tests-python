# Tests en Python

[![Build Status](https://travis-ci.org/JJ/tests-python.svg?branch=master)](https://travis-ci.org/JJ/tests-python)

Clase de prueba para enseñar a hacer tests en Python. 

## Instalando lo necesario

    pip install -r requirements.txt

## Para ejecutar los tests 

	pytest
	
## Para ejecutar

	python3 hugitos.py

o

	hug -f hugitos.py
	
## Usando docker

Primero (o cuando se quiera) se construye y ejecuta el volumen de
datos en [`data`](data/README.md)

A continuación

	sudo docker build -t minick/mitag .
	
Y para ejecutarlo (si se está ejecutando el volumen con el nombre `hitos`)

	sudo docker run -it --rm -p 8000:80 --volumes-from hitos jjmerelo/hugitos
	
`-rm` es necesario para que se borre una vez ejecutado, `-it` para que
se ejecute el terminal y salga el log y `-p 80:8000` es un *mapping*
del puerto del contenedor (80) al del host local
(8000). `--volumes-from hitos` monta el volumen que exporta el
contenedor `hitos`.

Se encuentra alojado en [Docker Hub](https://hub.docker.com/r/jjmerelo/tests-python/)

## Prueba

Despliegue: https://iv-2017.herokuapp.com/
Contenedor: https://tests-python-syboghyvul.now.sh

