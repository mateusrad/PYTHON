def somatorio(n):
    if n == 1:
        return 1
    return somatorio(n - 1) + n

num = int(input('digite um numero: '))

print(somatorio(num))