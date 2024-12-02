cont = 0
soma1 = 0
soma2 = 0
numeroteste = int(input(''))
while cont < numeroteste:
    cont = cont + 1
    apartir = int(input(''))
    valores = int(input(''))
    rangeimpar = valores * 2 - 1
    rangepar = valores * 2
    if apartir % 2 != 0:
        soma1 = 0
        for c in range(apartir, apartir + rangeimpar, 2):
            soma1 += c
        print(soma1)
    if apartir % 2 == 0:
        soma2 = 0
        for c in range(apartir + 1, apartir + rangepar, 2):
            soma2 += c
        print(soma2)

