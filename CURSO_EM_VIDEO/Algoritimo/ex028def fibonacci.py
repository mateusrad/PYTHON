def fibonacci(n):
    n_2 = n_1 = fib = 1
    while n > 1:
        fib = n_1 + n_2
        n = n - 1
        n_2 = n_1
        n_1 = fib
    return fib


n = 1
while n != 0:
    n = int(input('Entre com um valor (zero para sair): '))
    if n > 0:
        fib = fibonacci(n)
        print(f'fibonacci({n})= {fib}')


