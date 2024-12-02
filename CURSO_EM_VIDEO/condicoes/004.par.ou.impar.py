num1 = int(input('Digite um número:'))

par = num1 % 2

if par == 0:
    print('O número {} é um número Par'.format(num1))
else:
    print('O número {} é um número impar'.format(num1))