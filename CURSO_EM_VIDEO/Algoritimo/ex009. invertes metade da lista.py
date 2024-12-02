#Faça um programa em Python para inverter a primeira metade de uma string. O programa deve
# ler uma string, inverter a primeira metade (à esquerda) e salve a string com a nova configuração.

# Leitura da string
string_original = input("Digite uma string: ")

# Calcula o índice para a primeira metade
metade = len(string_original) // 2

# Inverte a primeira metade
string_invertida = string_original[:metade][::-1] + string_original[metade:]

# Exibe a string com a primeira metade invertida
print("String com a primeira metade invertida:", string_invertida)

