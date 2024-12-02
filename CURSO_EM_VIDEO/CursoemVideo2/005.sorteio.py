import random

alu1 = input('Digite o primeiro aluno:')
alu2 = input('Digite o segundo aluno:')
alu3 = input('Digite o terceiro aluno:')
alu4 = input('Digite o quarto aluno:')


lista = [alu1, alu2, alu3, alu4]

escolhido = random.choice(lista)

print('o escolhido foi {}'.format(escolhido))

