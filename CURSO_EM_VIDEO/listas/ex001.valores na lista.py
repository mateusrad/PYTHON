lista = []

for i in range(5):
    val = int(input(f'Digite o valor para a posição {i}:'))
    lista.append(val)
print(f'Você digitou os valores {lista}')

maior = max(lista)
print(f'O maior valor digitado foi {maior} na posição {i-1}')

menor = min(lista)
print(f'O menor valor digitado foi {menor} na posição {i -1}')



