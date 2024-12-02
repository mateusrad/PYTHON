A = input("Informe um valor para a variável A:" )
B= input("Informe o valor da variável B:" )

if (A>B):   #teste
    aux=A
    A=B
    B=aux

    print("O valor da variável A agora é : ", A)
    print("O valor da variável B agora é : ", B)
else:
    print("O valor da variável A é : ", A)
    print("O valor da variável B  é : ", B)