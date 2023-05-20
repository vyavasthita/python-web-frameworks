#!/bin/sh

echo "Running makemigrations"
python manage.py makemigrations

echo "Running migrate"
python manage.py migrate
# python manage.py migrate --database=mysql

echo "Create Super User"
python manage.py createsuperuser --no-input --username admin2 --email admin2@admin.com

echo "Running django server"
python manage.py runserver 0.0.0.0:5002
