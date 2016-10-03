#!/usr/bin/python

import os
import requests
import sys

tag = 'excited' if len(sys.argv) == 1 else sys.argv[1]
rating = 'pg'
out = tag if len(sys.argv) == 1 else sys.argv[2]

gifs_dir_exists = os.path.exists('./gifs')

if not gifs_dir_exists:
  os.mkdir('gifs')

os.chdir('gifs')

print('Looking for a ' + tag + ' gif...')

request = requests.get(
  'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC'
  + '&tag=' + tag
  + '&rating=' + rating
)

json = request.json()

image_url = json['data']['image_url']

img = requests.get(image_url)


with open(out + '.gif', 'w') as file: 
  file.write(img.content)
