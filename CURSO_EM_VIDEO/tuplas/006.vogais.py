palavra = ('carro', 'peixe', 'porta', 'tesoura',
           'goteira', 'lona', 'pedra')

for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')