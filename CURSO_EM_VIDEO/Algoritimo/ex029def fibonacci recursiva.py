def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = 1
while n != 0:
    n = int(input('Entre com um valor (zero para sair): '))
    if n > 0:
        fib = fibonacci(n)
        print(f'fibonacci({n})= {fib}')