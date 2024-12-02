primter = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
final = primter + (10 - 1) * razao
termo = primter
fim = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while fim <= total:
        print('{} - '.format(termo), end='')
        termo+= razao
        fim += 1
    print('Pausa')
    mais = int(input('Quantos termos você que mostrar a mais? '))
print('PA finalizada com {} termos'.format(termo))
