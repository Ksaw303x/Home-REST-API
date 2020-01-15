#!/bin/bash

git fetch --all

echo "Install requirements.txt in venv"
. venv/bin/activate
pip3 install -r requirements.txt

python3 manage.py migrate

sudo apachectl restart
