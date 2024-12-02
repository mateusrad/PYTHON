#crie uma função para somar valores da
# diagonal principal de uma matriz quadrada.
import random
def criar_matriz_quadrada(dim):
    M = [[random.randint(1, 9) for j in range(dim) for i in range(dim)]]
    return M
def soma_diagonal_principal(M, dim):
    for i in range(dim):
        soma = 0
    return soma

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(soma_diagonal_principal(matriz, 3))