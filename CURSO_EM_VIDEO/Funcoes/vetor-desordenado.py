def ordenar_decrescente(vetor):
    vetor_ordenado = sorted(vetor, reverse=True)
    return vetor_ordenado

numeros = [7, 9, 10, 8, 6]
numeros_ordenados = ordenar_decrescente(numeros)
print("Números ordenados em ordem decrescente:", numeros_ordenados)


