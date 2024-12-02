arquivo = open("números.txt", "r")   # abre arquivo números.txt para leitura

for linha in arquivo.readlines():    # gera uma lista contendo cada linha do arquivo
    print(linha)

arquivo.close()                      # fecha o arquivo "números.txt"