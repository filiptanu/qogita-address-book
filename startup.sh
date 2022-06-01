#!/bin/bash

python manage.py migrate

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@qogita.com
export DJANGO_SUPERUSER_PASSWORD=admin

python manage.py createsuperuser --noinput

export DJANGO_SUPERUSER_USERNAME=admin2
export DJANGO_SUPERUSER_EMAIL=admin2@qogita.com
export DJANGO_SUPERUSER_PASSWORD=admin2

python manage.py createsuperuser --noinput

python manage.py runserver
