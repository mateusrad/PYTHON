num1 = int(input(''))
num2 = int(input(''))
num3 = int(input(''))

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'{maior} eh o maior')
