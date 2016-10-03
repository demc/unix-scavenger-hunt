#!/usr/bin/python

import requests

request = requests.get(
  'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
)
json = request.json()

text = json['quoteText']
author = json['quoteAuthor']

author = author.lower().replace(' ', '_')

with open(author + '.txt', 'w') as file:
  file.write(text.encode('UTF-8'))
  file.write('\n')
