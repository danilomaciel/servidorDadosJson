__author__ = 'Dan'
import json
import requests
import urllib

print "Exclusao de Dados"
# Objeto contendo os dados para envio ao servidor.
dados ={

        "senha": "123456"
}

id= "5657941175b0ba782aa05d6e"
url = 'http://localhost:5000/clientes/'+ id

r = requests.delete(url)
resposta = r.content  # Content of response

print r.status_code  # Status code of response
print resposta
