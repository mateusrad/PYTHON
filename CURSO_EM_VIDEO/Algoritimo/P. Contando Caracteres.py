def mensagem_para_numeros(frase):
    palavras = frase.split()
    numeros = [str(len(palavra)) for palavra in palavras]
    resultado = '-'.join(numeros)
    return resultado
frase = input()
print(mensagem_para_numeros(frase))
