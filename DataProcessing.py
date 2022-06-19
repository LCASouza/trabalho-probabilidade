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


class DataProcessing:

    def __init__(self, arquivo: str):
        """
            Construtor: Classe DataProcessing

            Recebe como parâmetro:
                str arquivo:
                representa o endereço do arquivo de dados.
        """
        self.tabela = self.csv_file_reader(arquivo)

    def get_num_obitos(self):
        """
        Método para obter a quantidade de óbitos da tabela.

        Recebe como parâmetro:
            DataFrame tabela:
            tabela que possui os dados necessários.
        """
        obitos = []
        for linha in self.tabela["mortos"]:
            obitos.append(linha)
        return obitos

    def get_total_obitos(self):
        """
        Método para obter a quantidade total de óbitos.

        Recebe como parâmetro:
            DataFrame tabela:
            tabela que possui os dados necessários.
        """
        return sum(self.get_num_obitos())

    def get_data(self):
        """
        Método para obter as datas da tabela.

        Recebe como parâmetro:
            DataFrame tabela:
            tabela que possui os dados necessários.
        """
        data = []
        for linha in self.tabela["data_inversa"]:
            data.append(linha)
        return data

    def get_dia_semana(self):
        """
        Método para obter os dias da semana da tabela.

        Recebe como parâmetro:
            DataFrame tabela: tabela que possui os dados necessários.
        """
        dia_semana = []
        for linha in self.tabela["dia_semana"]:
            dia_semana.append(linha)
        return dia_semana

    def get_dia_semana_int(self):
        """
        Método para obter a contagem dos dias da semana da tabela.

        Recebe como parâmetro:
            list dias:
            lista com os dias da semana obtidos da tabela.
        """
        dias_semana_int = []

        for dia in self.tabela["dia_semana"]:
            if dia == "Domingo":
                dias_semana_int.append(0)
            if dia == "Segunda":
                dias_semana_int.append(1)
            if dia == "Terça":
                dias_semana_int.append(2)
            if dia == "Quarta":
                dias_semana_int.append(3)
            if dia == "Quinta":
                dias_semana_int.append(4)
            if dia == "Sexta":
                dias_semana_int.append(5)
            if dia == "Sábado":
                dias_semana_int.append(6)
        return dias_semana_int

    def get_horario(self):
        """
        Método para obter os horários da tabela.

        Recebe como parâmetro:
            DataFrame tabel:
            tabela que possui os dados necessários.
        """
        horario = []
        for linha in self.tabela["horario"]:
            horario.append(linha)
        return horario

    def get_pessoas_envolvidas(self):
        """
        Método para obter o número de pessoas envolvidas da tabela.

        Recebe como parâmetro:
            DataFrame tabela:
            tabela que possui os dados necessários.
        """
        pessoas = []
        for linha in self.tabela["pessoas"]:
            pessoas.append(linha)
        return pessoas

    def csv_file_reader(self, arquivo: str):
        """
        Método para ler um arquivo csv.

        Recebe como parâmetro:
            str arquivo:
            endereço/nome do arquivo que será lido.
        """
        dados = pd.read_csv(arquivo, sep=";")
        return dados

    def print_coluna(self, coluna: str):
        """
        Método para imprimir uma coluna da tabela.

        Recebe como parâmetros:
            DataFrame tabela:
            tabela que possui os dados para imprimir.

            str coluna:
            especifica a coluna que será impressa.
        """
        print(self.tabela[coluna])
