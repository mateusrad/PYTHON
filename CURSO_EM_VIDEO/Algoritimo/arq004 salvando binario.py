numeros = open("números.txt", "r")   # abre arquivo números.txt para leitura
impares = open("ímpares.bin", "wb")  # abre arquivo ímpares.bin para escrita binária

for linha in numeros.readlines():    # lista contendo cada linha do arquivo
    if int(linha) %2 != 0:
        valor = int(linha)           # converte a linha para valor inteiro
        impares.write(bytes(valor))   # converte de inteiro para bytes e salva

numeros.close()                      # fecha "números.txt"
impares.close()                      # fecha "ímpares.bin"