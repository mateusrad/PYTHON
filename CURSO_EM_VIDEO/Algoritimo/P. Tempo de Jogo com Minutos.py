hora_inicio = int(input())
minuto_inicio = int(input())
hora_final = int(input())
minuto_final = int(input())

minuto1 = hora_inicio * 60 + minuto_inicio
minuto2 = hora_final * 60 + minuto_final
jogo_em_minutos = minuto2 - minuto1

hora = 0
minuto = 0

if jogo_em_minutos > 0:
    hora = jogo_em_minutos // 60

if jogo_em_minutos <= 0:
    hora = (24 * 60 + jogo_em_minutos) // 60

if jogo_em_minutos % 60 > 0:
    minuto = jogo_em_minutos % 60

print(f'O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)')
