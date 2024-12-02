#Faça uma função troca() que recebe uma lista com dois valores e troca o conteúdo dos dois.
# Ou seja, o primeiro elemento da lista se transforma no segundo e o segundo se transforma no primeiro.
def troca(lista):
    if len(lista) == 2:
        lista[0], lista[1] = lista[1], lista[0]
        return lista
    else:
        print('')

valores = [1, 2]
print(troca(valores))
