#Faça uma função para calcular o fatorial de um número.
# Receba como parâmetro um número n e retorne como resposta n!
#Obs.: nome da função deve ser fatorial()
def fatorial(n):
    fatorial = 1
    for c in range(1, n + 1):
        fatorial *= c
    return fatorial


print(fatorial(5))
