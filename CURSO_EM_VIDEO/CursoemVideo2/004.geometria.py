import math

angulo = float(input('digite o angulo:'))
seno = math.sin(math.radians(angulo))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo,seno))

cosseno = math.cos(math.radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo,cosseno))

tangente = math.tan(math.radians(angulo))
print('o angulo {} tem a tangente {:.2f}'.format(angulo,tangente))
