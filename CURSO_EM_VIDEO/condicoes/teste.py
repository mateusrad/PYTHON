horaIni = int(input("Que horas o jogo iniciou: "))
horaFin = int(input("Que horas o jogo terminou: "))


if horaFin < horaIni:
    print(f"O JOGO DUROU {24 - horaIni + horaFin} HORA (S)")
else:
    if horaFin == horaIni:
        print("O JOGO DUROU 24 HORA (S)")
    else:
        print(f"O JOGO DUROU {horaFin - horaIni} HORA (S)")







