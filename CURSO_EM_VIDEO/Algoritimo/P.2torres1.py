distancia = int(input(''))
while distancia <= 0 or distancia > 10000:
    distancia = int(input(''))

diametro_palantir1 = int(input(''))
while diametro_palantir1 <= 0 or diametro_palantir1 > 100:
    diametro_palantir1 = int(input(''))

diametro_palantir2 = int(input(''))
while diametro_palantir2 <= 0 or diametro_palantir2 > 100:
    diametro_palantir2 = int(input(''))

icm = distancia / (diametro_palantir1 + diametro_palantir2)


print('{:.2f}'.format(icm))