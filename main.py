"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2007 - 2018

    ARQUIVO: main.py
"""

""" importações """
import string

from numpy import double
import data_processing as data
import graphics as gph
from Layout import Layout

def layoutChange(layout: Layout, tituloPrincipal: str, tituloX: str, tituloY: str, tituloXYSize: int, labelSize: int, tituloSize: int, barraSize: float):
    """
        layout: Objeto Layout

        tituloPrincipal: Título do Gráfico

        tituloX: Define o título do eixo horizontal

        tituloY: Define o título do eixo vertical

        tituloXYSize: Define o tamanho da fonte dos rótulos dos eixos vertical e horizontal

        labelSize: Define o tamanho dos elementos do gráfico

        tituloSize: Define o tamanho da fonte do título

        barraSize: Define o tamanho da barras do gráfico
    """
    layout.titulo = tituloPrincipal
    layout.axis_x_titulo = tituloX
    layout.axis_y_titulo = tituloY
    layout.axis_xy_titulo_size = tituloXYSize
    layout.label_size = labelSize
    layout.titulo_size = tituloSize
    layout.barras_size = barraSize


if __name__ == '__main__':
    tabela_acidentes = data.csv_file_reader("tabela_acidentes.csv")

    dias_semana = data.get_dia_semana_int(data.get_dia_semana(tabela_acidentes))

    layout = Layout()

    layoutChange(layout, 'Ocorrências de acidentes durante os dias da semana', 'dias da semana', 'quantidade de ocorrências', 10, 8, 15, 0.7)
    gph.mostrar_histograma_com_list(dias_semana, 7, layout)

    layoutChange(layout, 'Ocorrências de acidentes durante os dias da semana', 'quantidade de mortos', 'quantidade de ocorrências', 10, 8, 15, 0.7)
    gph.mostrar_histograma_com_dataframe(tabela_acidentes, "mortos", 20, layout)
