FROM bitnami/python:3.9
LABEL version="1.0.1" maintainer="JJMerelo@GMail.com"

ARG PORT
ENV PORT=${PORT:-31415}
RUN useradd -ms /bin/bash hugitos
USER hugitos
WORKDIR /home/hugitos

ENV PATH $PATH:/home/hugitos/.local/bin

RUN curl -sSL https://install.python-poetry.org | python -

ADD pyproject.toml .
ADD HitosIV/* HitosIV/
RUN poetry install

EXPOSE 31415

CMD [ "sh", "-c", "poetry run gunicorn --bind 0.0.0.0:${PORT} HitosIV.hugitos:__hug_wsgi__ --log-file -" ]
