vel = float(input('Digite a velocidade que o carro estava:'))
multa = (vel - 80) * 7.00
if vel > 80:
    print('Você estava dirigindo à {:.1f}km/h, esta velocidade está {:.1f}km/h acima do permitido '
          '\nVocê será multado em R${:.2f}'.format(vel,vel-80,multa))

print('Tenha um bom dia, dirija com segurança.')
