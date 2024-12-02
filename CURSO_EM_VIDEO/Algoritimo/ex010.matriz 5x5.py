#Faça um programa em Python para preencher uma matriz M de dimensão
# 5x5 com uma sequência numérica iniciando em 0 e adicionando
# valores coluna a coluna iniciando na primeira linha e terminando
# na quinta, conforme exemplo abaixo:

matriz = [[j + 6*i for j in range(6)] for i in range(6)]
print(matriz)