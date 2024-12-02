dist = float(input('Digite a distancia da viagem:'))

if dist <= 200:
    print('O valor a ser pago viagem será de R${:.2f}'.format(dist*0.5))
else:
    print('O valor a ser pago pela viagem será de R${:.2f}'.format(dist*0.45))
