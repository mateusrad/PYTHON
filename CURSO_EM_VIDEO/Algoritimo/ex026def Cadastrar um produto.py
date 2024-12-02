# Cadastro de Produtos - Meu Mercado

# Opções:
# 1. Cadastrar um produto
# 2. Listar todos os produtos
# 3. Buscar um produto
# 4. Buscar pelo nome do produto
# 5. Remover um produto
# 6. Comprar um produto
# 7. Comprar vários produtos

# criar um menu com as opções
def exibir_menu():
  print('''\n\nEscolha uma opção:

  1. Cadastrar um produto
  2. Listar produtos
  3. Buscar um produto
  4. Buscar pelo nome do produto
  5. Remover um produto
  6. Comprar um produto
  7. Comprar produtos
  0. Sair do programa
  ''')

# Função para cadastrar um produto
def cadastrar(produtos):
  codigo = int(input('Código do produto: '))
  nome = input('Nome do produto: ')
  preco = float(input('Preço do produto: '))
  estoque = int(input('Quantidade em estoque:'))
  produtos[codigo] = [nome, preco, estoque]

# Função para listar todos os produtos cadastrados
def listar(produtos):
  for produto in produtos:
    nome, preco, estoque = produtos[produto]
    print(f'Produto [{produto}]: {nome:10} - preço: R${preco:6.2f} - {estoque:5d} em estoque')

# Função para buscar um produto
def buscar(produtos):
  produto = int(input('Código: '))
  if produto in produtos:
    nome, preco, estoque = produtos[produto]
    print(f'Produto [{produto}]: {nome:10} - preço: R${preco:6.2f} - {estoque:5d} em estoque')
  else:
    print('Produto não encontrado!')

# Função para buscar/localizar um produto pelo nome
def buscarPorNome(produtos):
  nome_desejado = input('Nome do produto a buscar:')
  for produto in produtos:
    nome, preco, estoque = produtos[produto]
    if nome == nome_desejado:
      print(f'Produto [{produto}]: preço: R${preco:6.2f} - {estoque:5d} em estoque')
      return
  print(f'Produto "{nome_desejado}" não encontrado')

# Função para remover um produto
def remover(produtos):
  produto = int(input('Código: '))
  if produto in produtos:
    del produtos[produto]
  else:
    print('Produto não encontrado!')

# Comprar um produto se tiver quantidade em estoque
def comprar1(produtos):
  produto = int(input('Código: '))
  if produto in produtos:
    quantidade = int(input('Quantidade: '))
    nome, preco, estoque = produtos[produto]
    if quantidade <= estoque:
      custo = preco * quantidade
      print(f'Produto [{produto}]: {nome:10} - preço: {quantidade} x R${preco:6.2f} = R${custo:8.2f}')
      produtos[produto][2] -= quantidade
      return custo
    else:
      print(f'Quantidade solicitada não disponível! Temos {estoque} em estoque.')
  else:
    print('Produto não encontrado!')

# Comprar vários produtos tendo quantidade em estoque
def comprar(produtos):
  # lista primeiro todos os produtos
  listar(produtos)
  total = 0.0
  produto = int(input('Código do produto (-1 para fechar a sacola): '))
  while produto != -1:
    if produto in produtos:
      quantidade = int(input('Quantidade: '))
      nome, preco, estoque = produtos[produto]
      if quantidade <= estoque:
        custo = preco * quantidade
        print(f'Produto [{produto}]: {nome:10} - preço: {quantidade} x R${preco:6.2f} = R${custo:8.2f}')
        produtos[produto][2] -= quantidade
        total += custo
      else:
        print(f'Quantidade solicitada não disponível! Temos {estoque} em estoque.')
    else:
      print('Produto não encontrado!')
    produto = int(input('Código do produto (-1 para fechar a sacola): '))
  print(f'Total da compra: R${total:9.2f}')

# define alguns produtos para não precisar digitar toda vez
# código, nome, preço, estoque
produtos = {
    1: ['alface', 0.31, 200],
    2: ['tomate', 2.10, 1000],
    3: ['maçã', 9.87, 2000],
    4: ['batata', 1.05, 500]
}

# Loop principal (menu principal)
while True:
  exibir_menu()
  opcao = int(input('Escolha uma opção:'))
  if opcao == 1:
    cadastrar(produtos)
  elif opcao == 2:
    listar(produtos)
  elif opcao == 3:
    buscar(produtos)
  elif opcao == 4:
    buscarPorNome(produtos)
  elif opcao == 5:
    remover(produtos)
  elif opcao == 6:
    comprar1(produtos)
  elif opcao == 7:
    comprar(produtos)
  elif opcao == 0:
    break
  else:
    print('Opção Inválida!')
