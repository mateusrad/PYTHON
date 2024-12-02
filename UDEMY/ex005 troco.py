precoU = float(input('Preço unitário do produto: '))
qtd_produto = int(input('Quantidade comprada: '))
valor_pago = float(input('Dinheiro recebido: '))

custo = precoU * qtd_produto
troco = valor_pago - custo

print(f'TROCO = R${troco:.2f}')