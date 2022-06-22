"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2012 - 2014

    Graphics.py
    Classe para apresentação dos gráficos
"""

import matplotlib.pyplot as plt
from pandas import DataFrame
from Layout import Layout


class Graphics:

    def __init__(self):
        """
            Construtor: Classe Graphics
        """

    def mostrar_histograma_com_dataframe(self, dados: DataFrame, coluna: str, intervalo_coluna: int, layout: Layout):
        """
        Método para exibir um histograma usando uma tabela.

        Recebe como parâmetros:
            Data Frame dados:
            define os dados que serão utilizados no gráfico.

            str coluna:
            especifica a coluna que será plotada no histograma.

            int intervalo_coluna:
            intervalo entre das colunas do histograma.

            Layout Layout:
            contém os parâmetros para estilização do histograma.
        """
        dados.hist(column=coluna, bins=intervalo_coluna)
        plt.title(layout.titulo, fontsize=layout.titulo_size)
        plt.xlabel(layout.axis_x_titulo, fontsize=layout.axis_xy_titulo_size)
        plt.ylabel(layout.axis_y_titulo, fontsize=layout.axis_xy_titulo_size)
        plt.tick_params(labelsize=layout.label_size)
        plt.show()

    def mostrar_boxplot(self, dados: DataFrame, colunas: list, layout: Layout):
        """
        Método para exibir um boxplot.

        Recebe como parâmetros:
            Data Frame dados:
            define os dados que serão utilizados no gráfico.

            list colunas:
            especifica a(s) coluna(s) que será(ão) plotada(s) no boxplot.
        """
        dados.boxplot(column=colunas)
        plt.title(layout.titulo, fontsize=layout.titulo_size)
        plt.tick_params(labelsize=layout.label_size)
        plt.show()

    def mostrar_grafico_barras_dias_da_semana(self, dados: DataFrame):
        """
        Método para exibir um gráfico de barras.

        Recebe como parâmetro:
            DataFrame dados:
            contém os dados que serão utilizados no gráfico.
        """
        parameters = {'xtick.labelsize': 8,
                      'ytick.labelsize': 10,
                      'figure.figsize': (8, 6)}
        plt.rcParams.update(parameters)
        dados.plot.bar(rot=0, color='#175FFC')
        plt.title("Frequência dos acidentes durante os dias da semana", fontsize=15)
        plt.ylabel("Ocorrências", fontsize=12)
        plt.xlabel("Dias da semana", fontsize=12)
        plt.show()

    def mostrar_grafico_barras_acidentes(self, dados: DataFrame):
        """
        Método para exibir um gráfico de barras.

        Recebe como parâmetro:
            DataFrame dados:
            contém os dados que serão utilizados no gráfico.
        """
        parameters = {'xtick.labelsize': 8,
                      'ytick.labelsize': 10,
                      'figure.figsize': (10, 6)}
        plt.rcParams.update(parameters)

        alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
        legenda = []
        for causa_acidente, frequencia in dados.iteritems():
            letra = alfabeto.pop(0)
            plt.bar(letra, frequencia)
            legenda.append(letra + ' - ' + str(causa_acidente))

        plt.xlabel('Causas', fontsize=12)
        plt.ylabel('Ocorrências', fontsize=12)
        plt.title('Principais causas de acidentes nas rodovias federais (GO)')
        plt.legend(legenda)
        plt.show()

    def mostrar_grafico_vitimas_acidentes(self, dados: DataFrame):
        """
        Método para exibir um gráfico de barras.

        Recebe como parâmetro:
            DataFrame dados:
            contém os dados que serão utilizados no gráfico.
        """
        parameters = {'xtick.labelsize': 10,
                      'ytick.labelsize': 10,
                      'figure.figsize': (8, 6)}
        plt.rcParams.update(parameters)
        dados.plot.bar(rot=0, color='#06471F')
        plt.title("Vítimas dos acidentes nas rodovias federais (GO)", fontsize=15)
        plt.ylabel("Quantidade", fontsize=12)
        plt.show()

    def mostrar_grafico_causas_acidentes_vitimas(self, dados: DataFrame):
        """
        Método para exibir um gráfico de barras multiplas.

        Recebe como parâmetro:
            DataFrame dados:
            contém os dados que serão utilizados no gráfico.
        """
        parameters = {'xtick.labelsize': 8,
                      'ytick.labelsize': 13,
                      'figure.figsize': (15, 9)}
        plt.rcParams.update(parameters)
        dados.plot.bar()
        plt.title("Causas de acidentes X vítimas - rodovias federais (GO)", fontsize=20)
        plt.ylabel("Ocorrências", fontsize=15)
        plt.xlabel("Causas dos acidentes", fontsize=15)
        plt.legend(fontsize=15)
        plt.show()
