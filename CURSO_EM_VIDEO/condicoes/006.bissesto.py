ano = int(input('Digite o ano:'))

bisses = ano % 4

if bisses == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano de {} é um ano Bissesto'.format(ano))
else:
    print('O ano de {} não é um ano Bissesto'.format(ano))
