#faça um progtama que mostre a tabuada de um número
#que o usuario escolher utilizando laço (for)

num = int(input('Digite um número:'))

for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))