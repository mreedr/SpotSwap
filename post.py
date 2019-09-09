#!/bash/bin env python

import urllib2
import json

#URL = "http://192.168.1.66:8000"
URL = "http://localhost:8000/api/v1"

try:

  result = urllib2.urlopen(URL + '/entry/',
                           'location=Location1&'+
                           'dateinstalled=1990-01-01')
  content = result.read()
  print content
except urllib2.HTTPError, err:
  print err
