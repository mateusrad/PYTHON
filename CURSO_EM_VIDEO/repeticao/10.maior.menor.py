#faca um programa que leia o peso de cinco pessoas
#no final mostre qual foi o maior e o menor peso lido.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('{}-Qual é o seu peso?'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[031mO maior peso lindo foi {:.2f}kg'.format(maior))
print('\033[033mO menor pesos lido foi {:.2f}kg'.format(menor))

