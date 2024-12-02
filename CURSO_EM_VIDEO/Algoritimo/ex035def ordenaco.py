def maior(a, b):
    return a>b
def menor(a, b):
    return a<b
def igual(a, b):
    return a == b
def ordena(lista, func):
    tam = len(lista)
    for i in range(tam):
        for j in range(tam - 1):
            if func(lista[j], lista[j + 1]):
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux


l1 = [8, 1, 2, 3, 9, 0, 4, 20, 6, 5, 7]
ordena(l1,menor)
print(l1)