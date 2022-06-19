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
        self.tabela = self.csv_file_reader(arquivo)
        self.filtrar_uf_go()

    def get_num_obitos(self):
        """
        Método para obter a quantidade de óbitos da tabela.
        """
        obitos = []
        for linha in self.tabela["mortos"]:
            obitos.append(linha)
        return obitos

    def get_total_obitos(self):
        """
        Método para obter a quantidade total de óbitos.
        """
        return sum(self.get_num_obitos())

    def get_data(self):
        """
        Método para obter as datas da tabela.
        """
        data = []
        for linha in self.tabela["data_inversa"]:
            data.append(linha)
        return data

    def get_dia_semana(self):
        """
        Método para obter a contagem dos dias da semana da tabela.
        """
        return self.tabela.groupby(by='dia_semana').size()

    def get_horario(self):
        """
        Método para obter os horários da tabela.
        """
        horario = []
        for linha in self.tabela["horario"]:
            horario.append(linha)
        return horario

    def get_pessoas_envolvidas(self):
        """
        Método para obter o número de pessoas envolvidas da tabela.
        """
        pessoas = []
        for linha in self.tabela["pessoas"]:
            pessoas.append(linha)
        return pessoas

    def get_br(self):
        """
        Método para obter as rodovias presentes na tabela.
        """
        rodovia = []
        for linha in self.tabela["br"]:
            rodovia.append(linha)
        return rodovia

    def get_causa_acidentes_int(self):
        """
        Método para obter as principais causas de acidentes da tabela.
        """
        acidentes = []
        for linha in self.tabela["causa_acidente"]:
            if linha == "Velocidade incompatível":
                acidentes.append(0)
            if linha == "Falta de atenção":
                acidentes.append(1)
            if linha == "Ingestão de álcool":
                acidentes.append(2)
            if linha == "Não guardar distância de segurança":
                acidentes.append(3)
            if linha == "Desobediência à sinalização":
                acidentes.append(4)
            if linha == "Ultrapassagem indevida":
                acidentes.append(5)
            if linha == "Animais na Pista":
                acidentes.append(6)
            if linha == "Defeito mecânico em veículo":
                acidentes.append(7)
            if linha == "Defeito na via":
                acidentes.append(8)
            if linha == "Dormindo":
                acidentes.append(9)
        return acidentes

    def filtrar_uf_go(self):
        """
        Método para filtrar os dados da tabela para obter apenas dados de GO.
        """
        self.tabela = self.tabela.loc[self.tabela['uf'] == 'GO']
        self.tabela = DataFrame(self.tabela)

    def csv_file_reader(self, arquivo: str):
        """
        Método para ler um arquivo csv.

        Recebe como parâmetro:
            str arquivo:
            endereço/nome do arquivo que será lido.
        """
        dados = pd.read_csv(arquivo, sep=";", low_memory=False)
        return dados

    def print_coluna(self, coluna: str):
        """
        Método para imprimir uma coluna da tabela.

        Recebe como parâmetros:
            str coluna:
            especifica a coluna que será impressa.
        """
        print(self.tabela[coluna])
