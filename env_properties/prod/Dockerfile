FROM python:3

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=memes.settings_prod

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN /bin/bash -c "source env_properties/.env"

RUN pip install -r env_properties/base.txt
RUN pip install -r env_properties/prod/prod.txt
