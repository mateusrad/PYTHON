def rico_do_mate(N = int, L = float, Q = float, Nomes = list):
    cont = 0
    sobra = 0
    rico = ''
    i = 0

    while cont < L:
        cont += Q
        i += 1
        if round(cont,2) < L:
            rico = Nomes[int(i%N)]
            sobra = L - cont

    return print(f"{rico} {sobra:2.1f}")

rico_do_mate(3, 3.5, 0.3, ['Maria', 'Renato', 'Juca'])
rico_do_mate(3, 3.0, 0.3, ['Lara', 'Milena', 'Matheus'])
rico_do_mate(4, 3.0, 0.3, ['Lara', 'Milena', 'Matheus', 'Thiago'])
rico_do_mate(4, 4.5, 0.3, ['Lara', 'Milena', 'Matheus', 'Thiago'])
rico_do_mate(4, 4.7, 0.3, ['Lara', 'Milena', 'Matheus', 'Thiago'])