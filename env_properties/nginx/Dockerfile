FROM nginx

RUN adduser --system --no-create-home --shell /bin/false --group --disabled-login nginx
RUN apt-get install nano -y
#RUN apt-get install curl -y
#RUN apt-get install python2.7 -yf
#RUN API_KEY='447bd6cfefe2c4c7b7fbf9c5d82ad7d5' sh ./install.sh

ADD nginx.conf /etc/nginx/nginx.conf
