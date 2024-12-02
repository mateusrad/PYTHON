#Faça um algoritmo que leia o nome de 20 pessoas e exiba ao final a
# lista de nomes em ordem alfabética. Exiba um nome por linha.

pessoas = []

for n in range(20):
    pessoas.append(input('Digite um nome'))
pessoas.sort()
for c in pessoas:
    print(c)
