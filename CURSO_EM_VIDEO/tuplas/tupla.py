lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')


#forma simples, caso não precise da posição
for comida in lanche:
    print(f'Eu vou comer {comida}')
#OU
print('*'* 20)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

#fcaso precise da posição
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')


print('Comi pra caramba')
print(sorted(lanche))