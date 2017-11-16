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

	sudo docker build -t minick/mitag .
	
Y para ejecutarlo

	sudo docker run -p 80:8000 -it --rm minick/mitag
	
`-rm` es necesario para que se borre una vez ejecutado, `-it` para que
se ejecute el terminal y salga el log y `-p 80:8000` es un *mapping*
del puerto del contenedor (80) al del host local (8000).

Se encuentra alojado en [Docker Hub](https://hub.docker.com/r/jjmerelo/tests-python/)

## Prueba

Despliegue: https://iv-2017.herokuapp.com/
Contenedor: https://tests-python-syboghyvul.now.sh
