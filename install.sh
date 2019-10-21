#!/bin/bash

sudo apt update
sudo apt -y install python3
sudo apt -y install python3-pip

sudo apt -y install python3-venv
python3 -m venv venv

source venv/bin/activate

echo "Install requirements.txt"
pip3 install -r requirements.txt

deactivate