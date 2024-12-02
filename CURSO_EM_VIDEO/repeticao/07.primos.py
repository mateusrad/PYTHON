#faça um programa que leia um número inteiro e diga se ele
#é ou não um número primo

num = int(input('Digite um número:'))
primo = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end=' ')
        primo += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[mO número {} foi divisivel por {} vezes'.format(num,primo))
if primo == 2:
    print('Ele é primo')
else:
    print('O {} não é primo'.format(num))
