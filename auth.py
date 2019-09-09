#!/bash/bin env python
import urllib2, base64
import json

#URL = "http://192.168.1.66:8000"
URL = "http://localhost:8000/api/v1"
username = "bob"
password = "redfred"

request = urllib2.Request(URL + "/entry/")
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)
result = urllib2.urlopen(request)
print result







#try:

#  result = urllib2.urlopen(URL + '/entry/',
#                           'location=Location1&'+
#                           'dateinstalled=1990-01-01')
#  content = result.read()
#  print content
#except urllib2.HTTPError, err:
#  print err
