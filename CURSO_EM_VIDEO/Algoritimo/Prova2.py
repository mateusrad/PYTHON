matriz = []
for i in range(6):
    aux_linha = []
    for j in range(6):
        aux_linha.append(2*j + 3*i + i*j)
        if j == 5:
            matriz.append(aux_linha)

soma = 0
soma_quadrados_diff_media = 0
total_elementos = 0

for linha in matriz:
    for elemento in linha:
        soma += elemento
        total_elementos += 1

media = soma / total_elementos

for linha in matriz:
    for elemento in linha:
        soma_quadrados_diff_media += (elemento - media) ** 2

variancia = soma_quadrados_diff_media / total_elementos
desvio_padrao = variancia ** 0.5

print("Média:", round(media, 1))
print("Desvio padrão:", round(desvio_padrao, 3))
