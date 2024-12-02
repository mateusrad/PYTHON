#Escreva um algoritmo que permita a leitura de 7 números inteiros.
# Gere um vetor com os mesmos valores digitados mas de maneira invertida,
# ou seja, o primeiro número lido ficará na última posição do vetor.
# Exiba o vetor ao final colocando um número a cada linha.

num = [0]*7
numinv = [0]*7
for i in range(7):
    num[i] = int(input('Digite um número: '))

for i in range(7):
    numinv[i] = num[6 - i]

for i in range(7):
    print(numinv[i])