def multiplos(valor: int):
    if valor <= 2 or valor >= 50:
        return print("Valor inválido!")

    soma = 0
    for i in range(1, 101):
        if i % valor == 0:
            soma += i

    return print(soma)
print(multiplos(3))