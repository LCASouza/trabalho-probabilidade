"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2012 - 2014

    Graphics.py
    Classe para apresentação dos gráficos
"""

import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from Layout import Layout
from scipy.stats import norm


class Graphics:

    def __init__(self, dados: DataFrame):
        """
            Construtor: Classe Graphics

            Recebe como parâmetros:
                DataFrame tabela:
                define a tabela de dados para plotagem de gráficos usando DataFrame.
        """
        self.dados = dados

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
        self.dados.hist(column=coluna, bins=intervalo_coluna)
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
        self.dados.boxplot(column=colunas)
        plt.title(layout.titulo, fontsize=layout.titulo_size)
        plt.tick_params(labelsize=layout.label_size)
        plt.show()

    def mostrar_grafico_barras_dias_da_semana(self, dados: DataFrame):
        """
        Método para plotar um gráfico de barras.

        Recebe como parâmetro:
            DataFrame dados:
            contém os dados que serão plotados no gráfico.
        """
        # parameters = {'xtick.labelsize': 8,
        #               'ytick.labelsize': 10,
        #               'figure.figsize': (8, 6)}
        # plt.rcParams.update(parameters)
        # dados.plot.bar()
        # plt.title("Frequência dos acidentes durante os dias da semana", fontsize=15)
        # plt.ylabel("Ocorrências", fontsize=12)
        # plt.show()

    def mostrar_grafico_barras_acidentes(self, dados: DataFrame):
        """
        Método para plotar um gráfico de barras.

        Recebe como parâmetro:
            DataFrame dados:
            contém os dados que serão plotados no gráfico.
        """

        alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
        legenda=[]
        for causaAcidente, frequencia in dados.iteritems():
            letra = alfabeto.pop(0)
            plt.bar(letra , frequencia)
            legenda.append(letra +' - '+ causaAcidente)

        plt.xlabel('Tipo de acidentes')
        plt.ylabel('Frequência')
        plt.title('Gráfico de Acidentes')
        plt.legend(legenda)
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
