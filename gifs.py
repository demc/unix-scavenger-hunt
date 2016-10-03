#!/usr/bin/python

import os
import random
import subprocess
import sys

tags = [
  'angry'
  , 'bored'
  , 'shocked'
  , 'embarassed'
  , 'excited'
  , 'happy'
  , 'hungry'
  , 'inspired'
  , 'scared'
  , 'sad'
]

gifs_dir_exists = os.path.exists('./gifs')

count = 10 if len(sys.argv) == 1 else int(sys.argv[1])

if count > 10:
  count = 10

if gifs_dir_exists:
  exit()

for i in range(count):
  index = random.randint(0, 9)
  tag = tags[index]
  #print('getting gif for %s' %tag)   
  
  subprocess.call('python gif.py %s %d' % (tag, i), shell=True)

print('\nDone!')
