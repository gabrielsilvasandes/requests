# Deletar informação - DELETE

import requests

requisicao = requests.delete("https://teste-e7579-default-rtdb.firebaseio.com/-O_zR4fSKizJo2u2YC7P.json")

print(requisicao.json())

print("Informação DELETADA com sucesso!")
