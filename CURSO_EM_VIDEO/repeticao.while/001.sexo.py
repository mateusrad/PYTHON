sexo = input('Digite seu sexo [M/F]:').strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos, digite novamente o sexo [M/F]:').strip().upper()[0]

if sexo == 'F':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'


print('O sexo digitado foi {}.'.format(sexo))

