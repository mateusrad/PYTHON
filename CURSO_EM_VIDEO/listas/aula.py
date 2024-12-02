valores = list()
for cont in range(0, 5):
    valores.append((int(input('digite um valor:'))))

#valores.append(5)
#valores.append(9)
#valores.append(4)
valores.sort()
print(valores)
for c, v, in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('fim')