"""
Este programa realiza uma requisição POST para criar uma nova informação no
Firebase Realtime Database.

Autor: Gabriel Silva Sandes
Data: 2025-09-25

Fluxo:
    1. Criação de um dicionário Python com os dados desejados.
    2. Conversão do dicionário para JSON.
    3. Envio da requisição POST para o Firebase.
    4. Impressão da resposta retornada e confirmação da operação.

Variáveis:
    -> informacoes: dicionário com os dados que serão enviados ao banco.
    -> info: versão em JSON do dicionário 'informacoes'.
    -> requisicao: resposta da requisição POST ao Firebase.
"""

import json
import requests

informacoes = {
    "Nome":"Nathalia"
}

info = json.dumps(informacoes)

requisicao = requests.post("https://teste-e7579-default-rtdb.firebaseio.com/.json", data=info)

print(requisicao.json())

print("Informação CRIADA com sucesso!")
