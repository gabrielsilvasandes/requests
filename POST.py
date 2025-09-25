# Criar informação - POST

import json
import requests

informacoes = {
    "Nome":"Nathalia"
}

info = json.dumps(informacoes)

requisicao = requests.post("https://teste-e7579-default-rtdb.firebaseio.com/.json", data=info)

print(requisicao.json())

print("Informação CRIADA com sucesso!")
