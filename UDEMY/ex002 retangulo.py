import math
base = float(input('Base do retângulo: '))
altura = float(input('Altura do retângulo: '))

area = base * altura
perimetro = base * 2 + altura * 2
diagonal = math.sqrt(base ** 2 + altura ** 2)

print(f'ÁREA = {area:.4f}')
print(f'PERÍMETRO = {perimetro:.4f}')
print(f'DIAGONAL = {diagonal:.4f}')