primter = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
final = primter + (10 - 1) * razao
termo = primter
fim = 1

while fim <= 10:
    print('{} - '.format(termo), end='')
    termo+= razao
    fim += 1
print('Fim')


    
#for c in range(primter, final + razao, razao):
 #   print('{}'.format(c), end=' - ')
#print('Acabou')'''