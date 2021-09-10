#!/bin/bash
echo starting manage.py flush
echo .
python src/manage.py flush --noinput
echo 
echo creating superuser
echo ..
winpty python src/manage.py createsuperuser

echo 'Type '\''s'"'"' to skip compiling data'
read text
if [ $text = s ]
then
echo compiling data skipped
else
echo remove previous file and compile new one for import
rm -rf completed.xlsx
python script.py
fi
echo ...
echo
echo all job is done

echo 'Type '\''s'"'"' to skip running server'
read text
if [ $text = s ]
then
echo running server skipped
else
echo running server
python src/manage.py runserver
fi



