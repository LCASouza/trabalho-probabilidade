import csv
from operator import delitem

anoDaPesquisa = 2010

for i in range(5):
    anoDaPesquisa+=1
    with open("datatran{}.csv".format(anoDaPesquisa), "r") as arquivo:
        arquivoCsv = csv.reader(arquivo, delimiter = ";")
        for linha in arquivoCsv:
            print(linha)
