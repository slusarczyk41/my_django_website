build-prod:
	docker-compose -f prod-compose.yml build

build-dev:
	docker-compose -f dev-compose.yml build

up-prod:
	docker-compose -f prod-compose.yml up --build

up-dev:
	docker-compose -f dev-compose.yml up --build

ssh-django:
	docker exec -it django bash

ssh-server:
	docker exec -it nginx_server bash

install-docker:
	apt-get update
	apt-get install docker-compose -y

migrate:
	python manage.py makemigrations --noinput
	python manage.py migrate --noinput

staticfiles:
	python manage.py collectstatic --noinput
