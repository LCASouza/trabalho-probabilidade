"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2012 - 2014

    ARQUIVO: main.py
"""
import statistics
import numpy as np
from Graphics import Graphics
from DataProcessing import DataProcessing
from Layout import Layout

if __name__ == '__main__':

    tabela_acidentes = DataProcessing("arquivos/tabela_acidentes.csv")
    layout = Layout()
    graficos = Graphics(tabela_acidentes.tabela)

    layout.layout_change('Ocorrências de acidentes durante os dias da semana', 'dias da semana', 'quantidade de ocorrências', 10, 8, 15, 0.7)
    graficos.mostrar_histograma_com_list(tabela_acidentes.get_dia_semana_int(), 7, layout)

    layout.layout_change('Ocorrências de acidentes durante os dias da semana', 'quantidade de mortos', 'quantidade de ocorrências', 10, 8, 15, 0.7)
    graficos.mostrar_histograma_com_dataframe("mortos", 20, layout)

    layout.layout_change('Feridos graves nos acidentes', 'feridos graves', '', 10, 8, 15, 0.7)
    graficos.mostrar_boxplot(["feridos_graves"], layout)

    num = np.arange(0, 10, 0.01)
    media = np.mean(tabela_acidentes.get_dia_semana_int())
    dp = statistics.stdev(tabela_acidentes.get_dia_semana_int())
    graficos.mostrar_normal(num, float(media), dp)
