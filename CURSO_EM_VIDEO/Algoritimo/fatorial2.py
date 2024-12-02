num = int(input('Digite o número a ser fatorado:'))

fatorial = 1

for c in range(1,num+1):
    fatorial *= c
print('O fatorial de {} é {}'.format(num, fatorial))