num = 0
contador = 0
soma = 0
num = int(input('Digite um número:'))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número:'))
print('Voce digitou {} números e a soma entre eles fpi {}.'.format(contador, soma))


print(contador)



