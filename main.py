"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2007 - 2018

    ARQUIVO: main.py
"""

""" importações """
import data_processing as data
import graphics as gph

""" main    """
if __name__ == '__main__':
    tabela_acidentes_2007 = data.csv_file_reader("arquivos/datatran2007utf8.csv")
    tabela_acidentes_2008 = data.csv_file_reader("arquivos/datatran2008utf8.csv")
    tabela_acidentes_2009 = data.csv_file_reader("arquivos/datatran2009utf8.csv")
    tabela_acidentes_2010 = data.csv_file_reader("arquivos/datatran2010utf8.csv")

    #gph.mostrar_histograma(tabela_acidentes_2007, "mortos", 20)

    #print("Total de óbitos em 2007 = " + str(data.get_total_obitos(tabela_acidentes_2007)))

    #print(data.get_pessoas_envolvidas(tabela_acidentes_2007))

    gph.mostrar_histograma(tabela_acidentes_2007, "pessoas", 50)
