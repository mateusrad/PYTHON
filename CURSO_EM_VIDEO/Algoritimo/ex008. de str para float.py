#Fazer um programa para ler 10 strings contendo números ou expressões aritméticas.
# Após ler os strings, faça o Python avaliar as expressões e somar o resultado de todas as 10.
# Exiba o valor da soma ao final como ponto flutuante (float).

lista = []

for l in range(3):
    lista.append(eval(input('digite: ')))
print(sum(lista))

