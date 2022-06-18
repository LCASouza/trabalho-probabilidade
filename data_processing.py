"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2007 - 2018

    ARQUIVO: data_processing.py
        fornece tratamento para a base de dados

    Info:
    Base de dados disponível no diretório "arquivos/"
    Arquivos de dados devem estar no formato CSV UTF-8

"""

""" importações """
import pandas as pd
from datetime import datetime


def get_num_obitos(tabela):
    """
        Método para obter a quantidade de óbitos da tabela.
        Recebe como parâmetro:
            DataFrame tabela -> tabela que possui os dados necessários.
    """
    obitos = []
    for linha in tabela["mortos"]:
        obitos.append(linha)
    return obitos


def get_total_obitos(tabela):
    """
        Método para obter a quantidade total de óbitos.
        Recebe como parâmetro:
            DataFrame tabela -> tabela que possui os dados necessários.
    """
    return sum(get_num_obitos(tabela))


def get_data(tabela):
    """
        Método para obter as datas da tabela.
        Recebe como parâmetro:
            DataFrame tabela -> tabela que possui os dados necessários.
    """
    data = []
    for linha in tabela["data_inversa"]:
        data.append(linha)
    return data


def get_dia_semana(tabela):
    """
        Método para obter os dias da semana da tabela.
        Recebe como parâmetro:
            DataFrame tabela -> tabela que possui os dados necessários.
    """
    dia_semana = []
    for linha in tabela["dia_semana"]:
        dia_semana.append(linha)
    return dia_semana


def get_horario(tabela):
    """
        Método para obter os horários da tabela.
        Recebe como parâmetro:
            DataFrame tabela -> tabela que possui os dados necessários.
    """
    horario = []
    for linha in tabela["horario"]:
        horario.append(linha)
    return horario


def get_pessoas_envolvidas(tabela):
    """
            Método para obter o número de pessoas envolvidas da tabela.
            Recebe como parâmetro:
                DataFrame tabela -> tabela que possui os dados necessários.
    """
    pessoas = []
    for linha in tabela["pessoas"]:
        pessoas.append(linha)
    return pessoas


def csv_file_reader(arquivo):
    """
        Método para ler um arquivo csv.
        Recebe como parâmetro:
            str arquivo -> endereço/nome do arquivo que será lido.
    """
    tabela = pd.read_csv(arquivo, sep=";")
    return tabela

def csv_table_print(tabela, coluna):
    """
        Método para imprimir uma coluna da tabela.
        Recebe como parâmetros:
            DataFrame tabela -> tabela que possui os dados para imprimir.
            str coluna -> especifica a coluna que será impressa.
    """
    print(tabela[coluna])
