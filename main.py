#
#
#
#

#Reader para arquivo csv
#Recebe como parâmetro o nome do arquivo csv
def csv_file_reader(arquivo):
    import pandas as pd
    tabela = pd.read_csv(arquivo, sep=";")
    return tabela

if __name__ == "__main__":
    tabela = csv_file_reader("arquivos/datatran2007utf8.csv")
    print(tabela)
