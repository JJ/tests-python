# Tareas para este proyecto

## podman-images

> Crea imágenes de Docker a partir del Dockerfile usando Podman

~~~sh
podman build -f nodata.Dockerfile -t jjmerelo/hitos/data
podman build -f Dockerfile -t jjmerelo/hitos/hugitos
~~~

## start-pod

> Crea un pod con contenedores de Logstash y la aplicación

~~~bash
podman run -p 31415:31415 --pod new:hugitos --name hugitos_web --rm -dt jjmerelo/hitos/hugitos
export LOGSTASH_CONF_STRING='input {      tcp {     port => 8080 codec => json   } } output { stdout {} }'
podman run --pod hugitos --rm -dt --env LOGSTASH_CONF_STRING=$LOGSTASH_CONF_STRING --name logstash bitnami/logstash:latest
~~~

## destroy-pod

> Destruye el pod hugitos

~~~sh
podman pod stop hugitos
podman pod rm hugitos
~~~

## docker-images

> Crea imágenes de Docker a partir del Dockerfile

~~~sh
docker build . -f nodata.Dockerfile -t jjmerelo/hitos/data
docker build  -t jjmerelo/hitos/hugitos .
~~~
