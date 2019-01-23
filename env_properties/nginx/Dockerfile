FROM nginx

RUN adduser --system --no-create-home --shell /bin/false --group --disabled-login nginx
RUN apt-get update
RUN apt-get install nano -y

COPY env_properties/nginx/nginx.conf /etc/nginx/nginx.conf

RUN mkdir /code
RUN mkdir /code/static
WORKDIR /code
COPY ./static /code/static
