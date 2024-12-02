val1 = int(input('digite um valor:'))
val2 = int(input('digite um valor:'))
val3 = int(input('digite um valor:'))
val4 = int(input('digite um valor:'))

valores = (val1, val2, val3, val4)

print(f'Você digitou os valores {valores}')
print(f'O número 9 apareceu {valores.count(9)}')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ªposição')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram:', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')



