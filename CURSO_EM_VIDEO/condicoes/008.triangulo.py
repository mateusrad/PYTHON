reta1 = float(input('Digite a primeira reta:'))
reta2 = float(input('Digite a segunda reta:'))
reta3 = float(input('Digite a terceira reta:'))

if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print('Essas retas podem formar um trangulo')
else:
    print('Essas retas não podem formar um triangulo')
