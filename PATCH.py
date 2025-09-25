# Editar informação - PATCH

import json
import requests

informacoes = {
    "Nome":"Enzo"
}

info = json.dumps(informacoes)

requisicao = requests.patch("https://teste-e7579-default-rtdb.firebaseio.com/-O_zR4fSKizJo2u2YC7P.json", data=info)

print(requisicao.json())

print("Informação ATUALIZADA com sucesso!")
