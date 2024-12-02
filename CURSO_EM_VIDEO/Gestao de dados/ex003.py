def alg(nro):
    div = 0
    for i in range(1, nro + 1):
        if nro % i == 0:
            div += 1
    return div <=2

print(alg(4))

