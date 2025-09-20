#!/bin/bash

python3 manage.py makemigrations api
python3 manage.py makemigrations siteconfig
python3 manage.py makemigrations requirements
python3 manage.py makemigrations workitems
python manage.py makemigrations scheduler
python3 manage.py makemigrations testdesign
python3 manage.py makemigrations automation
python3 manage.py makemigrations execution
python3 manage.py makemigrations people
python3 manage.py makemigrations program
python3 manage.py migrate
