num1 = int(input('Digite um número:')) #entrada 1
num2 = int(input('Digite outro número:')) # entrada 2
operacao = 0

print('*'*25)
print('\033[033m[1]\033[034msomar\n\033[033m[2]\033[034mmultiplicar'
      '\n\033[033m[3]\033[34mmaior\n\033[33m[4]\033[34mnovos números'
      '\n\033[033m[5]\033[034msair do programa')
print('\033[m*'*25)
operacao = int(input('Qual opção você deseja:'))
if operacao > 5:
    print('Número invalido.')

if operacao == 4:
    while operacao == 4:
        print('Digite os valores e escolha a opção')
        num1 = int(input('Digite um número:')) #entrada 1
        num2 = int(input('Digite outro número:')) # entrada 2
        operacao = int(input('Qual opção você deseja:'))

if operacao == 1:
    soma = num1 + num2
    print('Resultado \n{} + {} = {}'.format(num1, num2, soma))
if operacao == 2:
    multiplicar = num1 * num2
    print('Resultado \n{} x {} = {}'.format(num1, num2, multiplicar))
if operacao == 3:
    if num1 > num2:
        print('O maior número inserido foi o {}'.format(num1))
    else:
        print('O maior número inserido foi o  {}'.format(num2,))
if operacao == 5:
    print('\033[031mPrograma encerrado')









