import csv
import json
import os
import time
from datetime import datetime
from random import random
from sys import argv

import pandas as pd
import seaborn as sns
import requests
import matplotlib.pyplot as plt

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados/ultimos/1?formato=json'


def extrair_taxa_cdi():
    try:
        response = requests.get(url=URL)
        response.raise_for_status()
    except requests.HTTPError:
        print("Dado não encontrado")
        return None
    except Exception as exc:
        print("Erro, finalizando execução")
        raise exc
    else:
        return json.loads(response.text)[-1]['valor']


def gerar_csv():
    dado = extrair_taxa_cdi()

    if not os.path.exists('./taxa-cdi.csv'):
        with open('./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
            fp.write('data,hora,taxa\n')

    for _ in range(10):
        data_e_hora = datetime.now()
        data = data_e_hora.strftime('%Y/%m/%d')
        hora = data_e_hora.strftime('%H:%M:%S')
        cdi = float(dado.replace(',', '.')) + (random() - 0.5)

        with open('./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
            fp.write(f'{data},{hora},{cdi:.4f}\n')

        time.sleep(1)

    print("CSV gerado com 10 registros.")


def gerar_grafico(nome_grafico):
    df = pd.read_csv('./taxa-cdi.csv')

    plt.figure(figsize=(10, 6))
    grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
    grafico.set_xticklabels(labels=df['hora'], rotation=90)
    grafico.set_title('Variação da Taxa CDI')
    grafico.set_xlabel('Hora')
    grafico.set_ylabel('Taxa')

    plt.tight_layout()
    grafico.get_figure().savefig(f"{nome_grafico}.png")
    print(f"Gráfico salvo como {nome_grafico}.png")


def main():
    if len(argv) < 2:
        print("Forneça o nome do gráfico como parâmetro.")
        return

    nome_grafico = argv[1]

    gerar_csv()
    gerar_grafico(nome_grafico)


if __name__ == "__main__":
    main()
