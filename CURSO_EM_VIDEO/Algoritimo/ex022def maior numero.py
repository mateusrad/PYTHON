#Crie uma função maior() que recebe três valores e retorna o maior dos três.
def maior(a, b, c):
    maior = a
    if b > a and b > c:
        maior = b
    if c > a and c > b:
        maior = c
    return maior


print(maior(130, 66, 35))