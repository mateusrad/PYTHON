dados = ['Pedro', 25, 'Maria', 19, 'João', 32]
pessoas = list()
pessoas.append(dados[:])
pessoas = [['Pedro', 25,], ['Maria', 19], ['Joao', 32]]


print(pessoas[0][0])
print(pessoas[1][1])
print(pessoas[2][1])


