cidade = input('Digite o nome da sua cidade:').upper().strip()

#print(cidade.find('SANTO'))

if cidade.find('SANTO') == 0:
    print('Santo faz parte do nome da cidade')
else:
    print('Santo não faz parte do nome da cidade')