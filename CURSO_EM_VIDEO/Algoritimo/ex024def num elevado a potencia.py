def pow(a, b):
    if b ==1:
        return a
    return a * pow (a, b-1)

nun = int(input('Digite o numero: '))
pot = int(input('Digite a potencia: '))


print(f'{nun} elevado a potencia {pot}\nÉ {pow(nun, pot)}')