#Faça um programa para:
#Criar uma matriz 5x4 preenchendo em cada célula a multiplicação dos índices da matriz. Por exemplo,
# na posição [2][3] será colocado o valor 6 (2x3);
#O programa deve ler 12 valores inteiros, representando 6 posições (e 3 pares de posições).
# A cada quatro valores, representando duas posições na matriz, faça a troca dos valores na matriz;
#Faça as três trocas (para os 3 pares de posições);
#Mostre a matriz ao final usando print(matriz).

# Criar a matriz 5x4
matriz = [[i * j for j in range(4)] for i in range(5)]

# Ler 12 valores inteiros e fazer as trocas
for _ in range(3):
    # Ler os valores para as posições a serem trocadas
    valores = [int(input("Digite um valor inteiro: ")) for _ in range(4)]

    # Extrair as posições da matriz
    linha1, coluna1, linha2, coluna2 = valores

    # Trocar os valores nas posições indicadas
    matriz[linha1][coluna1], matriz[linha2][coluna2] = matriz[linha2][coluna2], matriz[linha1][coluna1]
print(matriz)
