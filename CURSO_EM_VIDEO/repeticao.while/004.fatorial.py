import math

num = int(input('Digite um número:'))

#fatorial = math.factorial(num)
cont = num
fat = 1

while cont > 0:
    print('{} x '.format(cont), end='')
    fat *= cont
    cont -= 1
print('{}'.format(fat))



