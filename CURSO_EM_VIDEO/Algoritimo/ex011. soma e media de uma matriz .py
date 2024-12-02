#Faça um programa Python para somar todos os elementos da matriz
# do exercício anterior e calcular a média dos valores.
# Exiba ao final uma linha com a soma dos valores (valor inteiro) e
# outra linha com a média dos valores da matriz com uma casa decimal.

matriz = [[j + 5*i for j in range(5)] for i in range(5)]

soma = sum(elemento for linha in matriz for elemento in linha)
media = soma / (len(matriz)*5)
# Exibir a soma
print("Soma de todos os elementos:", soma)
print(media)


