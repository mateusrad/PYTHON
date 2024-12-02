#faça um programa que mostre na tela uma contagem regreciva
#para o estouro de fogos de artifícios, indo de 10 até 0, com
#com uma pausa de 1 segundo entre eles, utilizar biblioteca de delai
import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('já')

