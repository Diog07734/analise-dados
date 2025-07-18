import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
