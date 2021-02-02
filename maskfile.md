# Tareas para este proyecto

## podman-images

> Crea imágenes de Docker a partir del Dockerfile usando Podman

~~~sh
podman build -f nodata.Dockerfile -t jjmerelo/hitos/data
podman build -f Dockerfile -t jjmerelo/hitos/hugitos
~~~

## docker-images

> Crea imágenes de Docker a partir del Dockerfile

~~~sh
docker build . -f nodata.Dockerfile -t jjmerelo/hitos/data
docker build  -t jjmerelo/hitos/hugitos .
~~~
