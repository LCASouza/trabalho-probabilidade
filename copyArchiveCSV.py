import pandas as pd
import data_processing as data

tabela_acidentes_2012 = data.csv_file_reader("arquivos/datatran2007utf8.csv")
tabela_acidentes_2013 = data.csv_file_reader("arquivos/datatran2008utf8.csv")
tabela_acidentes_2014 = data.csv_file_reader("arquivos/datatran2009utf8.csv")
tabela_acidentes_2015 = data.csv_file_reader("arquivos/datatran2010utf8.csv")

final = pd.DataFrame

final += tabela_acidentes_2012
final += tabela_acidentes_2013
final += tabela_acidentes_2014
final += tabela_acidentes_2015

print(final)