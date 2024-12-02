#desenvolva um programa que leia o nome, idade e sexo
#de quatro pessoas. no final do programa mostre:
#media de idade do grupo
#nome do home mais velho
#quantas mulheres tem menos de 21 anos
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1, 3):
    print('--------{}ª PESSOA---------'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = input('Sexo [M/F]:').strip()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome


mediaidade = somaidade // 3
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))



