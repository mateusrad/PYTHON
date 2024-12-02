n = int(input())
for l in range(n):
    sobrenome = input().capitalize()
    dificil = False

    percorrer = len(sobrenome) - 2

    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for l in range(percorrer):
        if sobrenome[l] not in vogais:
            if sobrenome[l + 1] not in vogais:
                if sobrenome[l + 2] not in vogais:
                    dificil = True
    if dificil:
        print(f'{sobrenome} nao eh facil')
    else:
        print(f'{sobrenome} eh facil')
