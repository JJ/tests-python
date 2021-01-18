FROM bitnami/python:3.9
LABEL version="1.0.1" maintainer="JJMerelo@GMail.com"

RUN useradd -ms /bin/bash hugitos
USER hugitos
WORKDIR /home/hugitos
ENV PATH=$PATH:/home/hugitos/.poetry/bin

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ADD pyproject.toml .
ADD data/hitos.json data/
ADD HitosIV/* HitosIV/
RUN poetry install


EXPOSE 31415

ENTRYPOINT [ "poetry",  "run", "HitosIV.hugitos:__hug_wsgi__", "--log-file", "-" ]
