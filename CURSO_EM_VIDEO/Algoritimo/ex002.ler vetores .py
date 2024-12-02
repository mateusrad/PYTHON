#Crie um programa em Python para ler dois vetores de 15 posições
#de inteiros cada e mostre a interseção dos vetores.
# Primeiro faça a leitura dos 15 valores inteiros para o primeiro
# vetor e depois os 15 valores do segundo. Lembrando que intersecção
# são elementos repetidos em ambos sem repetição (observe que os valores iguais
# normalmente não estarão na mesma posição). Para facilitar, considere que os valores não se
# repetem dentro do mesmo vetor.

# Leitura do primeiro vetor
vetor1 = []
print("Digite os valores do primeiro vetor:")
for i in range(15):
    elemento = int(input(f'Digite o valor {i + 1}: '))
    vetor1.append(elemento)

# Leitura do segundo vetor
vetor2 = []
print("Digite os valores do segundo vetor:")
for i in range(15):
    elemento = int(input(f'Digite o valor {i + 1}: '))
    vetor2.append(elemento)

# Encontrar a interseção dos vetores preservando a ordem original
intersecao = [elemento for elemento in vetor1 if elemento in vetor2]

# Exibir a interseção na ordem original
print("Interseção dos vetores na ordem original:")
for elemento in intersecao:
    print(elemento)
