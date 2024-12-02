nome = input('Digite seu nome completo:').strip()

print(f'Seu nome maiusculo é {nome.upper()}')
print(f'Seu nome minusculo é {nome.lower()}')
nome_junto = (''.join(nome.split()))
prim_nome = nome.split()[0]
print(f'Se nome sem espaços é {nome_junto}')


qtd_letras = len(nome_junto)
print(f'Seu nome tem um total de {qtd_letras} letras')
print(f'Seu primeiro nome é {prim_nome.upper()} e tem {len(prim_nome)} letras')
