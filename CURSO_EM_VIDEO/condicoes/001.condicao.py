
nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
nota3 = float(input('Digite sua terceira nota:'))

media = (nota3 + nota2 + nota1) / 3

if media >= 7:
    print('Sua media é {:.1f}, você está Aprovado'.format(media))
else:
    print('Sua média é de {:.1f}, você foi Reprovado'.format(media))


