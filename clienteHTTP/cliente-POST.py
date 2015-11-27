__author__ = 'Dan'
import json
import requests
import urllib

print "Inclusao de Dados"
# Objeto contendo os dados para envio ao servidor.
dados ={

        "nome": "Pedro Pedreira",
        "idade": "50",
        "endereco": "Av. Sampaio Vidal",
        "senha": "123456",
}



url = 'http://localhost:5000/clientes'
headers = {'content-type': 'application/json'}
r = requests.post(url, dados)
resposta = r.content  # Content of response

print r.status_code  # Status code of response
print resposta
