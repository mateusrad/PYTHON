def criar_matriz(linas = 3, colunas = 3):
    M = [[0 for j in range(colunas)] for i in range(linas)]
    return M

M4x5 = criar_matriz(4, 5)
print(len(M4x5))