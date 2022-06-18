"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2007 - 2018

    ARQUIVO: graphics.py
        Realiza a plotagem dos gráficos
"""

""" importações """
import matplotlib.pyplot as plt


def mostrar_histograma_com_dataframe(tabela, coluna, num_colunas, layout):
    """
    Método para plotar um histograma usando uma tabela.

    Recebe como parâmetros:
        DataFrame tabela:
        tabela que possui os dados necessários para plotar o histograma.

        str coluna:
        especifica a coluna que será plotada no histograma.

        int num_colunas:
        especifica a quantidade de colunas que serão plotadas.

        Layout Layout:
        contém os parâmetros para estilização do histograma.
    """
    tabela.hist(column=coluna, bins=num_colunas)
    plt.title(layout.titulo, fontsize=layout.titulo_size)
    plt.xlabel(layout.axis_x_titulo, fontsize=layout.axis_xy_titulo_size)
    plt.ylabel(layout.axis_y_titulo, fontsize=layout.axis_xy_titulo_size)
    plt.tick_params(labelsize=layout.label_size)
    plt.show()


def mostrar_histograma_com_list(lista, num_barras, tam, layout):
    """
    Método para plotar um histograma usando uma lista.

    Recebe como parâmetros:
        list lista:
        lista que possui os dados necessários para plotar o histograma.

        int num_barras:
        especifica a quantidade de barras do histograma.

        int tam:
        especifica o tamanho relativo das barras.

        Layout Layout:
        contém os parâmetros para estilização do histograma.
    """
    plt.hist(lista, num_barras, rwidth=tam)
    plt.title(layout.titulo, fontsize=layout.titulo_size)
    plt.xlabel(layout.axis_x_titulo, fontsize=layout.axis_xy_titulo_size)
    plt.ylabel(layout.axis_y_titulo, fontsize=layout.axis_xy_titulo_size)
    plt.tick_params(labelsize=layout.label_size)
    plt.show()


def mostrar_boxplot(tabela, colunas):
    """
    Método para plotar um boxplot.

    Recebe como parâmetros:
        DataFrame tabela:
        tabela que possui os dados necessários para plotar o boxplot.

        str colunas:
        especifica a(s) coluna(s) que será(ão) plotada(s) no boxplot.
    """
    tabela.boxplot(column=colunas)
    plt.show()
