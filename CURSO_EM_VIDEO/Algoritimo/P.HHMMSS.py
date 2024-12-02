#Leia um valor inteiro, que é o tempo de duração em segundos de
# um determinado evento em uma fábrica, e informe-o expresso no
# formato horas:minutos:segundos.

segundos = int(input(''))
if segundos <= 0:
    while segundos < 0:
        segundos = int(input(''))

hora = 0
minuto = 0
if segundos < 60:
    print('{:}:{:}:{:}'.format(hora, minuto, segundos))
if segundos >= 60 and segundos < 3600:
    minuto = segundos // 60
    segundos = (segundos % 60)
    print('{:}:{:}:{:}'.format(hora, minuto, segundos))
if segundos >= 3600:
    hora = segundos // 3600
    minuto = (segundos % 3600) // 60
    segundos = (segundos - (hora * 3600))% 60
    print('{}:{}:{}'.format(hora, minuto, segundos))




