#crie um progama que leia o ano de nascimento de sete pessoas
#no final mostre quantas pessoas ainda nao atingiram a maioridade
#e quantas ja são maiores
#considere maior idade com 21 anos
import datetime
atual = datetime.date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu?'.format(c)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('\033[34mAo todo tivemos {} pessoas maiores de idade.'.format(maior))
print('\033[31mAo todo tivemos {} pessoas menores de idade.'.format(menor))




