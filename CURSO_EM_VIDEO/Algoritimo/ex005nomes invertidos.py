#Escreva um algoritmo que permita a leitura de 7 nomes e coloque em uma lista.
# Exiba a lista de trás para frente, exibindo no início o último nome informado
# e o ao final da lista o primeiro. Exiba um nome a cada linha.

nomes = []
for n in range(1, 8):
    nomes.append(input(f'Digite o {n}º nome: '))

nomesinver = nomes[::-1]
for c in nomesinver:
    print(c)
