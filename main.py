"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2012 - 2014

    ARQUIVO: main.py
"""

from Graphics import Graphics
from DataProcessing import DataProcessing

if __name__ == '__main__':

    tabela = DataProcessing("arquivos/tabela_acidentes.csv")
    graficos = Graphics()

    graficos.mostrar_grafico_barras_dias_da_semana(tabela.get_dia_semana())

    graficos.mostrar_grafico_barras_acidentes(tabela.get_causa_acidentes())

    graficos.mostrar_grafico_vitimas_acidentes(tabela.get_vitimas_acidentes())

    graficos.mostrar_grafico_causas_acidentes_vitimas(tabela.get_causas_acidentes_sum_vitimas())
