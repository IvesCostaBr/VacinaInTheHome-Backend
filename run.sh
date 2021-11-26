#!/bin/bash

sudo apt-get install python3-venv -y
sudo apt install python3-pip -y
sudo python3 -m venv venv
$(source ./venv/bin/activate)
pip3 install -r requirements.txt

python3 manage.py runserver