"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2007 - 2018

    ARQUIVO: graphics.py
        Realiza a plotagem dos gráficos
"""

""" importações """
import matplotlib.pyplot as plt


def mostrar_histograma(tabela, coluna, num_colunas):
    """
        Método para plotar um histograma.
        Recebe como parâmetros:
            DataFrame tabela -> tabela que possui os dados necessários para plotar o histograma.
            str coluna -> especifica a coluna que será plotada no histograma.
            num_colunas -> especifica a quantidade de colunas que serão plotadas.
    """
    tabela.hist(column=coluna, bins=num_colunas)
    plt.show()
