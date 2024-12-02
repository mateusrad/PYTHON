resp = 'Ss'
media = qtd = soma = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número:'))
    soma += num
    qtd += 1
    resp = input('Quer continuar? ').upper().strip()[0]
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

media = soma/ qtd
print('Voce digitou {} e média foi {:.1f}'.format(qtd, media))
print('O maior número digita do foi {} e o nemor foi {}.'.format(maior, menor))







