lar = float(input('Digite a largura da parede:'))
alt = float(input('Digite a altura da parede:'))
area = lar*alt
tin = 2
print('Sua parede tem {:.2f}m.A por {:.2f}m.L\nSua área total é de {:.2f}m²'.format(alt,lar,area))
print('Serão necessárias {:.0f} litros de tinta para realizar toda a pintura'.format(area//tin))
