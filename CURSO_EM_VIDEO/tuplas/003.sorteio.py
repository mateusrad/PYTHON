import random

valores = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
       random.randint(1, 10), random.randint(1, 10))



print(f'Os valores sorteados foram:', end='')
for n in valores:
    print(f'{n}', end=' ')

print(f'\nO valor 9 apareceu {valores.count(9)}')
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O menor valor foi o {min(valores)}')
#print(f'O valor 3 está na posição {valores.index(3)}')