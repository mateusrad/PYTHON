def ordena_por_tamanho(lista_strings):
    return sorted(lista_strings, key=lambda x: (len(x), lista_strings.index(x)))

print(ordena_por_tamanho(['dois', 'três', 'um']))