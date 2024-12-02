c = float(input('Digite a temperatura em graus célcius:'))

f = c*1.8+32
k = c+273.15

print('{:.2f}°célcius corresponde a'.format(c))
print('{:.2f}°fahrenheit\n{:.2f}°kelvin'.format(f,k))
