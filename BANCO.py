"""
Este programa consulta a API do Banco Central (serviço Olinda) para obter
informações sobre o dinheiro em circulação no Brasil.

Autor: Gabriel Silva Sandes
Data: 2025-09-25

Fluxo:
    1. Requisição da API do BCB (dinheiro em circulação).
    2. Extração de informações principais: Data, Espécie, Denominação e Valor.
    3. Formatação da data para padrão brasileiro (DD/MM/AAAA).
    4. Conversão das variáveis para cálculos numéricos.
    5. Exibição do resultado no formato de moeda brasileira.

Variáveis:
    -> informacoes: resposta JSON recebida da API.
    -> valores: lista com os dados retornados (dicionários).
    -> valoresData: data original retornada pela API.
    -> formatacaoData / dataFormatada: data ajustada para exibição.
    -> especie: espécie do dinheiro (ex.: moeda metálica, cédula).
    -> moeda: denominação da moeda em reais.
    -> contMoeda: quantidade ou valor em circulação da denominação.
    -> valorFinal: valor total calculado em reais.
"""

import requests
from pprint import pprint

url = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=2&$format=json&$select=Data,Quantidade,Valor,Denominacao,Especie"

requisicao = requests.get(url)
informacoes = requisicao.json()
valores = informacoes["value"]

valoresData = valores[0]["Data"]
formatacaoData = valoresData.replace('1994', '3') + valoresData.replace('3', '1994')
dataFormatada = f"0{formatacaoData[0]}/{formatacaoData[2:4]}/{formatacaoData[7:11]}"

especie = valores[0]["Especie"]
moeda = valores[0]["Denominacao"]
contMoeda = valores[0]["Valor"]

moeda = moeda.replace("'", "")
moeda = float(moeda)
contMoeda = float(contMoeda)
valorFinal = moeda * contMoeda
moeda = str(moeda)
contMoeda = str(contMoeda)

print(f"Em {dataFormatada}, a quantidade de R$[{moeda}] em circulação no Brasil era de {contMoeda}. Totalizando: R${valorFinal:.2f}")
