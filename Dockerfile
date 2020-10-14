FROM python:3
LABEL version="1.0.0" maintainer="JJMerelo@GMail.com"

WORKDIR /usr/src/app

COPY requirements.txt ./
ADD data/hitos.json data/
ADD HitosIV/* HitosIV/

RUN pip install --no-cache-dir -r requirements.txt && \
        rm requirements.txt

EXPOSE 80

ENTRYPOINT [ "hug",  "-p 80", "-f", "HitosIV/hugitos.py" ]