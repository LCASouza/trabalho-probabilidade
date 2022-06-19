"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2007 - 2018

    ARQUIVO: main.py
"""
import statistics
import numpy as np
from Graphics import Graphics
from DataProcessing import DataProcessing
from Layout import Layout


def layout_change(layout: Layout, titulo_principal: str, titulo_x: str, titulo_y: str, titulo_xy_size: int, label_size: int, titulo_size: int, barra_size: float):
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
    layout.titulo = titulo_principal
    layout.axis_x_titulo = titulo_x
    layout.axis_y_titulo = titulo_y
    layout.axis_xy_titulo_size = titulo_xy_size
    layout.label_size = label_size
    layout.titulo_size = titulo_size
    layout.barras_size = barra_size


if __name__ == '__main__':

    tabela_acidentes = DataProcessing("arquivos/tabela_acidentes.csv")
    layout = Layout()
    graficos = Graphics(tabela_acidentes.tabela)

    layout_change(layout, 'Ocorrências de acidentes durante os dias da semana', 'dias da semana', 'quantidade de ocorrências', 10, 8, 15, 0.7)
    graficos.mostrar_histograma_com_list(tabela_acidentes.get_dia_semana_int(), 7, layout)

    layout_change(layout, 'Ocorrências de acidentes durante os dias da semana', 'quantidade de mortos', 'quantidade de ocorrências', 10, 8, 15, 0.7)
    graficos.mostrar_histograma_com_dataframe("mortos", 20, layout)

    layout_change(layout, 'Feridos graves nos acidentes', 'feridos graves', '', 10, 8, 15, 0.7)
    graficos.mostrar_boxplot(["feridos_graves"], layout)


