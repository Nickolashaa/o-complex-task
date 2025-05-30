#!/bin/bash
python manage.py makemigrations weather
python manage.py migrate
DJANGO_SUPERUSER_USERNAME=admin \
DJANGO_SUPERUSER_EMAIL=admin@example.com \
DJANGO_SUPERUSER_PASSWORD=admin \
python manage.py createsuperuser --noinput
exec python manage.py runserver 0.0.0.0:8000
