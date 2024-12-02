numeros = open("números.txt", "r")   # abre arquivo números.txt para leitura
pares = open("pares.txt", "a")       # abre arquivo pares.txt para escrita

for linha in numeros.readlines():    # lista contendo cada linha do arquivo
    if int(linha) %2 != 0:
        pares.write(linha)           # linha já tem o '\n'

numeros.close()                      # fecha "números.txt"
pares.close()                        # fecha "pares.txt"