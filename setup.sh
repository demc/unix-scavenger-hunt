#!/bin/bash

echo "Setting up requirements..."

wget https://goo.gl/K7hvzs -O /tmp/requirements.txt
sudo apt-get install python-pip -y
pip install -r /tmp/requirements.txt

echo "Setting up scripts..."

wget https://raw.githubusercontent.com/demc/unix-scavenger-hunt/master/gif.py -O gif.py
wget https://raw.githubusercontent.com/demc/unix-scavenger-hunt/master/gifs.py -O gifs.py
