def mdc(a, b):
    if a < b:
        return mdc(b, a)
    elif b == 0:
        return a
    else:
        return mdc(b, a%b)

num1 = int(input('digite um numero:'))
num2 = int(input('digite um numero:'))

print(mdc(num1, num2))