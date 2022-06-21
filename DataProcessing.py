"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2012 - 2014

    DataProcessing.py
    Classe para tratamento da base de dados

    INFO:
    Base de dados disponível no diretório "arquivos".
    Arquivos de dados devem estar no formato CSV UTF-8.

"""
import pandas as pd
from pandas import DataFrame


class DataProcessing:

    def __init__(self, arquivo: str):
        """
            Construtor: Classe DataProcessing

            Recebe como parâmetro:
                str arquivo:
                representa o endereço do arquivo de dados.
        """
        self.dados = self.csv_file_reader(arquivo)
        self.filtrar_uf_go()

    def get_dia_semana(self):
        """
        Método para obter a quantidade de acidentes nos dias da semana.
        """
        return self.dados.groupby(by='dia_semana', sort=False).size()

    def get_vitimas_acidentes(self):
        """
        Método para obter a quantidade de vítimas da tabela.
        """
        d = {'Vítimas': [self.dados['feridos_graves'].sum(),
                         self.dados['feridos_leves'].sum(),
                         self.dados['mortos'].sum(),
                         self.dados['ilesos'].sum()]}

        return pd.DataFrame(data=d, index=['Feridos graves', 'Feridos leves', 'Óbitos', 'Ilesos'])

    def get_causa_acidentes(self):
        """
        Método para obter as principais causas de acidentes da tabela.
        """
        return self.dados.groupby(by='causa_acidente').size()

    def filtrar_uf_go(self):
        """
        Método para filtrar os dados da tabela para obter apenas dados de GO.
        """
        self.dados = DataFrame(self.dados.loc[self.dados['uf'] == 'GO'])

    def csv_file_reader(self, arquivo: str):
        """
        Método para ler um arquivo csv.

        Recebe como parâmetro:
            str arquivo:
            endereço/nome do arquivo que será lido.
        """
        dados = pd.read_csv(arquivo, sep=";", low_memory=False)
        return dados
