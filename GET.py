"""
Este programa realiza uma requisição GET para buscar informações armazenadas
no Firebase Realtime Database.

Autor: Gabriel Silva Sandes
Data: 2025-09-25

Fluxo:
    1. Envia uma requisição GET para a URL base do Firebase.
    2. Recebe e imprime todas as informações armazenadas no banco de dados.
    3. Exibe uma mensagem de confirmação ao final.

Variáveis:
    -> requisicao: resposta da requisição GET ao Firebase.
"""

import requests

requisicao = requests.get("https://teste-e7579-default-rtdb.firebaseio.com/.json")

print(requisicao.json())

print("REQUISIÇÃO realizada com sucesso!")
