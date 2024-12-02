func = float(input('Digite o valor do seu salário R$'))

if func > 1250.00:
    print('Você terá um aumento de 10%, seu novo salário será de R${:.2f}'.format(func+(func*10/100)))
else:
    print('Você terá um aumento de 15%, seu novo salário será de R${:.2f}'.format(func+(func*15/100)))

