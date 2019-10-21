#!/bin/bash

git fetch --all

echo "Install requirements.txt"
pip3 install -r requirements.txt

python3 manage.py migrate