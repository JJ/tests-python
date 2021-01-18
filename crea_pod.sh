#!/bin/bash

podman run -p 31415:31415 --pod new:hugitos --name hugitos_web --rm -dt jjmerelo/hugitos:test
export LOGSTASH_CONF_STRING='input {      tcp {     port => 8080     codec => json   } } output { stdout {} }'
podman run --pod hugitos --rm -dt --env LOGSTASH_CONF_STRING=$LOGSTASH_CONF_STRING --name logstash bitnami/logstash:latest
