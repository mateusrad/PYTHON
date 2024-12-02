#Faça um algoritmo que leia um vetor de 30 elementos inteiros
# e exiba o mesmo em ordem crescente. Imprima (exiba) um valor por linha.

tabela = []

for t in range(1, 31):
    num = int(input(''))
    tabela.append(num)
tabela.sort()

for num in tabela:
    print(num)
