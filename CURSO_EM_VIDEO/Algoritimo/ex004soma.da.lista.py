#Fazer um programa para ler um vetor de 10 números inteiros,
# somar estes valores e exibir a soma.

vetor = []
soma = 0

for c in range(1, 11):
    num = int(input('digite um número:'))
    soma += num
vetor = soma
print(vetor)

