km = float(input('Quantos km o carro percorreu?'))
alu = int(input('Por quantos dias o carro foi alugado?'))

vdia = 60
kmr = 0.15

print('O carro foi alugado por {} e rodou por {}km\nO valor total a pagar pelo aluguel é de R${:.2f}'
      .format(alu,km,(alu*vdia)+(km*kmr)))
