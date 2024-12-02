def farorial(n):
    if n == 1:
        return 1
    return n * farorial(n - 1)

n = int(input('Digite um numero para fatorar: '))

print(f'O fatorial de {n} é {farorial(n)}')