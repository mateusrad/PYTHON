valorP = float(input('Digite o valor do produto:R$'))
desc = valorP*5/100
print('O valor do produto sem o desconto é R${:.2f}\nO valor do produto com o desconto de 5% é R${:.2f}'.format(valorP,valorP-desc))
