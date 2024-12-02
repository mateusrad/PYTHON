#Desenvolva uma função somatorio(n) para calcular a soma de todos
# os valores ímpares de 1 até o número indicado. Ex. somatorio(10)
# deve retornar 25 (1+3+5+7+9).
def somatorio(n):
    resultado = 0
    for i in range(1, n + 1, 2):
        resultado += i
    return resultado

# Exemplo de uso da função

print(somatorio(10))
