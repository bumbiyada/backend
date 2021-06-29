#!/bin/bash
python src/manage.py flush
winpty python src/manage.py createsuperuser
python src/manage.py migrate
