# Volumen con datos

Mini-Dockerfile para crear un volumen con datos.

Para construirlo

	sudo docker build -t jjmerelo/hitos  .
	
(O cualesquiera nombre y nick que quieras asignarle)

Para ejecutarlo y que se pueda usar el volumen de datos en otro lado

	sudo docker run --rm -it --name hitos jjmerelo/hitos
	
con lo que se comenzará a ejecutar con el nombre `hitos` y se podrá
usar para exportar el volumen de datos montado.
