import math

co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
#hi = math.sqrt(co**(2) + ca**(2))
hi = math.hypot(co,ca)

print('o valor da hipotenuza é {:.2f}'.format(hi))
print('')

