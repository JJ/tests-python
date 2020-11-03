# Tests en Python

[![Build Status](https://travis-ci.com/JJ/tests-python.svg?branch=master)](https://travis-ci.com/JJ/tests-python)

Clase de prueba para enseñar a hacer tests en Python.

## Instalando lo necesario

Este repositorio usa `poetry` como gestor de dependencias y, hasta
cierto punto, de tareas.

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

El volumen "de datos" tiene que ejecutarse también para poder usarse:

	sudo docker run -d -it --rm jjmerelo/datos sh

(`-d` es para ejecutar en background, y se ejecuta `sh` para que haya un proceso ejecutándose todo el tiempo).

Para saber cual es el nombre del contenedor, se ejecuta `sudo docker ps`. La primera columna da un `CONTAINER ID` y la última un `NAME`. Para *montar* ese contenedor de datos desde otro contenedor "ejecutable" habrá que hacer

	sudo docker run -it --rm -p 8000:80 --volumes-from curious_name jjmerelo/hugitos

Donde `curious_name` es el nombre que aparece, para ese contenedor en ejecución, en la columna `NAME`. También se pueden usar los primeros números del `CONTAINER ID`de la primera columna.

`-rm` es necesario para que se borre una vez ejecutado, `-it` para que
se ejecute el terminal y salga el log y `-p 80:8000` es un *mapping*
del puerto del contenedor (80) al del host local
(8000). `--volumes-from hitos` monta el volumen que exporta el
contenedor `hitos`.

Se encuentra alojado en [Docker Hub](https://hub.docker.com/r/jjmerelo/tests-python/)

## Prueba

Despliegue: https://iv-2017.herokuapp.com/
Contenedor: https://tests-python-syboghyvul.now.sh

