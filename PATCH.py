"""
Este programa realiza uma requisição PATCH para editar uma informação existente
no Firebase Realtime Database.

Autor: Gabriel Silva Sandes
Data: 2025-09-25

Fluxo:
    1. Criação de um dicionário Python com os novos dados.
    2. Conversão do dicionário para JSON.
    3. Envio da requisição PATCH para atualizar o registro específico no Firebase.
    4. Impressão da resposta retornada e confirmação da operação.

Variáveis:
    -> informacoes: dicionário com os dados que serão atualizados.
    -> info: versão em JSON do dicionário 'informacoes'.
    -> requisicao: resposta da requisição PATCH ao Firebase.
"""

import json
import requests

informacoes = {
    "Nome":"Enzo"
}

info = json.dumps(informacoes)

requisicao = requests.patch("https://teste-e7579-default-rtdb.firebaseio.com/-O_zR4fSKizJo2u2YC7P.json", data=info)

print(requisicao.json())

print("Informação ATUALIZADA com sucesso!")
