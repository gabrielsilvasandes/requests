"""
Este programa realiza uma requisição DELETE para remover uma informação
específica do Firebase Realtime Database.

Autor: Gabriel Silva Sandes
Data: 2025-09-25

Fluxo:
    1. Envia uma requisição DELETE para a URL do item específico no Firebase.
    2. Remove permanentemente o dado correspondente.
    3. Exibe a resposta do servidor e uma mensagem de confirmação.

Variáveis:
    -> requisicao: resposta da requisição DELETE ao Firebase.
"""

import requests

requisicao = requests.delete("https://teste-e7579-default-rtdb.firebaseio.com/-O_zR4fSKizJo2u2YC7P.json")

print(requisicao.json())

print("Informação DELETADA com sucesso!")
