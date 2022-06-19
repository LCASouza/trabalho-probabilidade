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


