#Faça uma função chamada multiplos7(inicio,fim)
# que retorna a SOMA dos múltiplos de 7 entre um valor
# inicial e um valor final (inclusive).
def multiplos7(a, b):
    soma = 0
    for i in range(a, b + 1):
        if i % 7 == 0:
            soma += i
    return soma


print(multiplos7(7, 7))

