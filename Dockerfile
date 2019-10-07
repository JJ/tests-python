FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir HitosIV data
ADD data/hitos.json data/
ADD HitosIV/* HitosIV/

CMD [ "hug",  "-p 80", "-f","HitosIV/hugitos.py" ]

EXPOSE 80
