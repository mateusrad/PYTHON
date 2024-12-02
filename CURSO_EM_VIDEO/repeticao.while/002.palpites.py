import random
import time

computador = random.randint(0, 10)
print('\033[033m*' *40)
print('Vou escolher um número entre {} e {}.\nTente adivinhar qual será este número'.format(0, 10))
print('\033[033m*'*40)
jogador = int(input('\033[mEscolha um número entre {} e {}:'.format(0, 10)))
print('Processando')
time.sleep(1)
palpites = 1
while jogador != computador:
    if jogador > computador:
        print('É um número menor que este')
    else:
        print('É um número maior que este')
    jogador = int(input('\033[mEscolha outro número entre {} e {}:'.format(0, 10)))
    print('Processando')
    time.sleep(1)
    palpites += 1
print('\033[034mParabéns você acertou com {} palpites.'.format(palpites))
