tabela = ('Palmeira', 'Botafogo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Flamengo',
          'Athletico-PR', 'Fluminense', 'Cuiabá', 'São Paulo', 'Corinthias', 'Fortaluza',
          'Internacional', 'Santos', 'Vasco', 'Bahia', 'Cruzeiro', 'Goias', 'Coritiba',
          'Améria-MG')

#for t in tabela:
    #print(t)
print(f'Essa é a tabela do brasileirão 2023 {tabela}')
print('=*='*50)
print(f'Os cinco primeiros colocados são: {tabela[:6]}')
print('=*='*50)
print(f'Os ultimos quatro colocados são: {tabela[-4:]}')
print('=*='*50)
print(f'Os times em ordem alfabética {sorted(tabela)}')
print(f'O time do Bahia está na {tabela.index("Bahia")+1}ª posição')
