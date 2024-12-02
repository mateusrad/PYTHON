def par(n):
    if n == 0:
        return True
    return impar(n - 1)

def impar(n):
    if n == 0:
        return False
    return par(n - 1)

for i in range(30):
    impar(i)
    if impar(i) == True:
        print(f'{i} é impar?', impar(i))


for i in range(30):
   par(i)
   if par(i) == True:
        print(f'{i} é par?', par(i))