import random
import time

inic = int(input('Digite o número inicial:'))
filn = int(input('Digite o número final:'))

computador = random.randint(inic, filn)
print('*' *50)
print('Vou escolher um número entre {} e {}.\nTente adivinhar qual será este número'.format(inic,filn))
print('*'*50)
jogador = int(input('Escolha um número entre {} e {}:'.format(inic,filn)))
print('Processando')
time.sleep(5)

if jogador == computador:
    print('Parabéns você acertou')
else:
    print('Eu Ganhei!, você escolheu o número {}, mas eu havia escolhido o número {}'.format(jogador,computador))




