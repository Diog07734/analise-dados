import extracao
import visualizacao
import sys

def main():
    if len(sys.argv) < 2:
        print("Forneça o nome do gráfico como argumento.")
        return

    nome_grafico = sys.argv[1]

    extracao.gerar_csv()
    visualizacao.gerar_grafico(nome_grafico)


if __name__ == "__main__":
    main()
