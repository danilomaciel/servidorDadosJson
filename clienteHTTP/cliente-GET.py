import json
from urllib2 import URLError
from urllib2 import HTTPError
import urllib2
import requests


r = requests.get("http://localhost:5000/")
data = r.content  # Content of response

print r.status_code  # Status code of response
print data
