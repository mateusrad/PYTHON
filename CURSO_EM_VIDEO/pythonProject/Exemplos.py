qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor:" ))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("Digite o valor:" ))

media = soma / qtd
print("\n total da soma: ", soma)
print("\r quantidade de valores digitados:", qtd)
print("\r Média dos valores:", media)
