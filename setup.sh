#!/bin/bash

echo "Setting up requirements..."

wget https://goo.gl/K7hvzs -qO /tmp/requirements.txt
sudo apt-get -qq install python-pip -y
pip install -r -q /tmp/requirements.txt

echo "Setting up scripts..."

wget https://raw.githubusercontent.com/demc/unix-scavenger-hunt/master/gif.py -qO gif.py
wget https://raw.githubusercontent.com/demc/unix-scavenger-hunt/master/gifs.py -qO gifs.py

sudo chmod +x gif.py gifs.py
