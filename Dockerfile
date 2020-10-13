FROM python:3
LABEL version="1.0.0" maintainer="JJMerelo@GMail.com"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

RUN mkdir HitosIV data
ADD data/hitos.json data/
ADD HitosIV/* HitosIV/

CMD [ "hug",  "-p 80", "-f","HitosIV/hugitos.py" ]

EXPOSE 80
