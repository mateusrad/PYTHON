largura = float(input('Digite a largura do terreno:'))
comprimento = float(input('Digite o comprimento do terreno: '))
valor_metro = float(input('Digite o valor do m²: '))

area = comprimento * largura
preco = area * valor_metro

print(f'Área do terreno = {area:.2f}m²')
print(f'Preço do terreno = R${preco:.2f}')