nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

media = (nota2 + nota1)/2

if media >= 7:
    print('Sua média é {:.2f}, você está {}.'.format(media,'Aprovado'))
else:
    print('Sua média é {:.2f}, você está {}.'.format(media,'Reprovado'))

