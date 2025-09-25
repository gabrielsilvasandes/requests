# Pegar informação - GET

import requests

requisicao = requests.get("https://teste-e7579-default-rtdb.firebaseio.com/.json")

print(requisicao.json())

print("REQUISIÇÃO realizada com sucesso!")
