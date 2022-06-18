"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2007 - 2018

    ARQUIVO: Layout.py
        Classe para estilização dos layouts dos gráficos
"""

""" importações """


class Layout:

    def __init__(self):
        """
        titulo: Título do Gráfico

        axis_x_titulo: Define o título do eixo horizontal

        axis_y_titulo: Define o título do eixo vertical

        titulo_size: Define o tamanho da fonte do título

        axis_xy_titulo_size: Define o tamanho da fonte dos rótulos dos eixos vertical e horizontal

        label_size: Define o tamanho dos elementos do gráfico

        barras_size: Define o tamanho da barras do gráfico
        """
        self.titulo = "titulo"
        self.axis_x_titulo = "x_titulo"
        self.axis_y_titulo = "y_titulo"
        self.titulo_size = 10
        self.axis_xy_titulo_size = 8
        self.label_size = 10
        self.barras_size = 1
