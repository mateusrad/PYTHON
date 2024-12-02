real = float(input('Quantos reais você tem na carteria? R$'))

dolar = 4.95
euro = 5.26

print('Com R${:.2f}\nVocê pode comprar US${:.2f}\nVocê pode comprar EUR${:.2f}'.format(real,real/dolar,real/euro))


