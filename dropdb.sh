#!/bin/bash
echo starting manage.py flush
echo .
python src/manage.py flush
echo 
echo creating superuser
echo ..
winpty python src/manage.py createsuperuser
echo
echo remove previous file and compile new one for import
echo ...
rm -rf completed.xlsx
python script.py
echo
echo all job is done

echo running server

python src/manage.py runserver
