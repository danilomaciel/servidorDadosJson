import json
import requests


r = requests.get("http://localhost:5000/clientes")
data = r.content  # Content of response

print r.status_code  # Status code of response
print data
