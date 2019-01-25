FROM python:3

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=memes.settings_dev
RUN bash source env_properties/.env.sh

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -r env_properties/base.txt
RUN pip install -r env_properties/dev/dev.txt

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput
