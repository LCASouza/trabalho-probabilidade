"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2007 - 2018

    Graphics.py
    Classe para apresentação dos gráficos
"""

import matplotlib.pyplot as plt
from pandas import DataFrame
from Layout import Layout
from scipy.stats import norm


class Graphics:

    def __init__(self, tabela: DataFrame):
        self.tabela = tabela

    def mostrar_histograma_com_dataframe(self, coluna: str, intervalo_coluna: int, layout: Layout):
        """
        Método para plotar um histograma usando uma tabela.

        Recebe como parâmetros:
            str coluna:
            especifica a coluna que será plotada no histograma.

            int intervalo_coluna:
            intervalo entre das colunas do histograma.

            Layout Layout:
            contém os parâmetros para estilização do histograma.
        """
        self.tabela.hist(column=coluna, bins=intervalo_coluna)
        plt.title(layout.titulo, fontsize=layout.titulo_size)
        plt.xlabel(layout.axis_x_titulo, fontsize=layout.axis_xy_titulo_size)
        plt.ylabel(layout.axis_y_titulo, fontsize=layout.axis_xy_titulo_size)
        plt.tick_params(labelsize=layout.label_size)
        plt.show()

    def mostrar_histograma_com_list(self, lista: list, num_barras: int, layout: Layout):
        """
        Método para plotar um histograma usando uma lista.

        Recebe como parâmetros:
            list lista:
            lista que possui os dados necessários para plotar o histograma.

            int num_barras:
            especifica a quantidade de barras do histograma.

            Layout Layout:
            contém os parâmetros para estilização do histograma.
        """
        plt.hist(lista, num_barras, rwidth=layout.barras_size)
        plt.title(layout.titulo, fontsize=layout.titulo_size)
        plt.xlabel(layout.axis_x_titulo, fontsize=layout.axis_xy_titulo_size)
        plt.ylabel(layout.axis_y_titulo, fontsize=layout.axis_xy_titulo_size)
        plt.tick_params(labelsize=layout.label_size)
        plt.show()

    def mostrar_boxplot(self, colunas: list, layout: Layout):
        """
        Método para plotar um boxplot.

        Recebe como parâmetros:
            list colunas:
            especifica a(s) coluna(s) que será(ão) plotada(s) no boxplot.
        """
        self.tabela.boxplot(column=colunas)
        plt.title(layout.titulo, fontsize=layout.titulo_size)
        plt.tick_params(labelsize=layout.label_size)
        plt.show()

    def mostrar_normal(self, dados, media: float, desv_padrao: float):
        """
            Método para plotar uma curva normal.

            Recebe como parâmetros:
                list dados:
                lista de dados para plotagem do gráfico da curva normal.
                INFO: a lista de dados deve ser do tipo int ou float.

                float media:
                define a media para plotagem do gráfico da curva normal.

                float desv_padrao:
                define o desvio padrão para plotagem do gráfico da curva normal.
        """
        plt.plot(dados, norm.pdf(dados, media, desv_padrao))
        plt.show()
