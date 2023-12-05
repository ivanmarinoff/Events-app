#!/bin/sh

echo "Install the dependencies"
pip install -r requirements.txt


echo "Running Database Migrations"
python manage.py makemigrations
python manage.py migrate

echo "Running app management commands"

python manage.py runserver 0.0.0.0:8000
exec "$@"