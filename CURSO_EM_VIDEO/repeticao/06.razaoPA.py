#desenvolva um programa que leia o primeiro termo e a razão
#de uma PA. no final, mostre os 10 primeiros termos dessa progressao.

primter = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
final = primter + (10 - 1) * razao


for c in range(primter, final + razao, razao):
    print('{}'.format(c), end=' - ')
print('Acabou')
