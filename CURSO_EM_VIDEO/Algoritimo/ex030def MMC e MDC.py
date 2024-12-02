def calcular_mdc(a, b):
   while b:
      a, b = b, a % b
   return a


def calcular_mmc(a, b):
   if a == 0 or b == 0:
      return 0
   else:
      return abs(a * b) // calcular_mdc(a, b)


# Exemplo de uso:
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

mmc_resultado = calcular_mmc(num1, num2)

print(f"O MMC de {num1} e {num2} é: {mmc_resultado}")

