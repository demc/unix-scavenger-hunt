#!/usr/bin/python

import requests
import sys

#if len(sys.argv) > 1:
#  print(sys.argv[1])
sentence = None
sentence = None if len(sys.argv) == 1 else sys.argv[1]
headers = {'X-Mashape-Key': 'TUSDlMBgNpmshvTuhhg78PLlYQ1Wp10jTxqjsnhh4uIWzfRGHa'}

if sentence: 
  yodaish = requests.get(
    'https://yoda.p.mashape.com/yoda?'
    + 'sentence=' + sentence
    , headers=headers
  )

  print(yodaish.text)
