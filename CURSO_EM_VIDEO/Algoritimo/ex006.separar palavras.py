#Crie um programa em Python para ler uma frase,
# separar palavra por palavra e exibir cada palavra em uma linha.

frase = input('Digite uma frase:')
frase_separada = frase.split()

for p in frase_separada:
   print(p)
