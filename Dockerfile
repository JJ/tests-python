FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY HitosIV.py hugitos.py ./

CMD [ "hug",  "-p 80", "-f","hugitos.py" ]

EXPOSE 80
