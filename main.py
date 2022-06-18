"""
    Pontifícia Universidade Católica de Goiás
    Trabalho de Probabilidade e Estatística - MAF1730 C01
    Análise de Dados - Acidentes nas rodovias federais 2007 - 2018

    ARQUIVO: main.py
"""

""" importações """
import data_processing as data
import graphics as gph
from Layout import Layout


if __name__ == '__main__':
    tabela_acidentes_2007 = data.csv_file_reader("arquivos/datatran2007utf8.csv")
    tabela_acidentes_2008 = data.csv_file_reader("arquivos/datatran2008utf8.csv")
    tabela_acidentes_2009 = data.csv_file_reader("arquivos/datatran2009utf8.csv")
    tabela_acidentes_2010 = data.csv_file_reader("arquivos/datatran2010utf8.csv")

    #gph.mostrar_histograma(tabela_acidentes_2007, "mortos", 20)

    #print("Total de óbitos em 2007 = " + str(data.get_total_obitos(tabela_acidentes_2007)))

    #print(data.get_pessoas_envolvidas(tabela_acidentes_2007))

    #gph.mostrar_histograma(tabela_acidentes_2007, "pessoas", 50)

    #gph.mostrar_boxplot(tabela_acidentes_2007, "mortos")

    #data.get_dia_semana_int(data.get_dia_semana(tabela_acidentes_2007))

    dias_semana = data.get_dia_semana_int(data.get_dia_semana(tabela_acidentes_2007))

    layout = Layout()
    layout.titulo = "Ocorrências de acidentes durante os dias da semana"
    layout.axis_x_titulo = "dias da semana"
    layout.axis_y_titulo = "quantidade de ocorrências"
    layout.axis_xy_titulo_size = 10
    layout.label_size = 8
    layout.titulo_size = 15

    gph.mostrar_histograma_com_list(dias_semana, 7, 0.9, layout)
