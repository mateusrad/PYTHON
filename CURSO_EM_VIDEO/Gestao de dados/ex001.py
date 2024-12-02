def alg(nro):
    resposta = 0
    for i in range(1, nro):
        resposta = resposta + i
    return resposta


print(alg(5))