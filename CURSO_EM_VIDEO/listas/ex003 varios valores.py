lista = []
valor = 0
continuar = 'S'

while continuar == 'S':
    valor = int(input('Digite um valor:'))
    lista.append(valor)
    continuar = input('Deseja continuar? S/N:')
