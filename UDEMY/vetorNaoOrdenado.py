import numpy as np


class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, " - ", self.valores[i])

    # O(1) - O(2)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade máxima atingia")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1



vetor = VetorNaoOrdenado(10)


print("insere o numero 3,2,4,5,6,1")
vetor.insere(3)
vetor.insere(2)
vetor.insere(4)
vetor.insere(5)
vetor.insere(6)
vetor.insere(1)
vetor.imprime()
print("-" * 50)

print("pesquisa o numero 5")
print(vetor.pesquisar(5))
print("-" * 50)

print("pesquisa o numero 9")
print(vetor.pesquisar(9))
print("-" * 50)

print("exclui o numero 5")
vetor.excluir(5)
vetor.imprime()
print("-" * 5)


vetor.insere(11)

vetor.imprime()
