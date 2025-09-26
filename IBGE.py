"""
Este programa consulta a API do IBGE para obter o IRSM (Índice de Reajuste do
Salário Mínimo) referente a junho de 1994.

Autor: Gabriel Silva Sandes
Data: 2025-09-25

Fluxo:
    1. Requisição da API do IBGE (agregados de inflação).
    2. Extração da variável consultada (IRSM - Percentual no mês).
    3. Seleção da série temporal correspondente a junho de 1994.
    4. Conversão do período em ano e mês.
    5. Exibição do valor da inflação formatado em texto.

Variáveis:
    -> informacoes: resposta JSON recebida da API.
    -> variavel: nome da variável consultada (IRSM).
    -> serie: dicionário contendo o período e valor da inflação.
    -> periodo: string com o ano e mês concatenados (AAAAMM).
    -> valor: valor da inflação no período selecionado.
    -> numeroMes: número do mês extraído do período.
    -> nomeMes: nome do mês (aqui fixado como "Junho").
"""

import requests
from pprint import pprint

url = "https://servicodados.ibge.gov.br/api/v3/agregados/90/periodos/199406/variaveis/64?localidades=N1[all]&classificacao=73[2639]"

requisicao = requests.get(url)

informacoes = requisicao.json()

variavel = informacoes[0]["variavel"]
serie = informacoes[0]["resultados"][0]["series"][0]["serie"]

periodo, valor = list(serie.items())[0]

numeroMes = periodo[4:] 
nomeMes = numeroMes = "Junho"

print(f"O {variavel} {nomeMes} do ano de {periodo[0:4]} registrou {valor}% de inflação mensal.")
