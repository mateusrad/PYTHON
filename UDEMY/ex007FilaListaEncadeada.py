import numpy as np

class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None

  def mostra_no(self):
    print(self.valor)

class ListaEncadeada:
  def __init__(self):
    self.primeiro = None

  def __lista_vazia(self):
    return self.primeiro == None

  def insere_final(self, valor):
      novo = No(valor)
      if self.__lista_vazia():
          self.primeiro = novo
      else:
          self.ultimo.proximo = novo
          novo.anterior = self.ultimo
      self.ultimo = novo

  def excluir_inicio(self):
    if self.primeiro == None:
      print('A lista está vazia')
      return None
    temp = self.primeiro
    self.primeiro = self.primeiro.proximo
    return temp

  def mostrar_frente(self):
      atual = self.primeiro
      while atual != None:
          atual.mostra_no()
          atual = atual.proximo


class FilaListaEncadeada:
  def __init__(self):
    self.lista = ListaEncadeada()

  def enfileirar(self, valor):
    self.lista.insere_final(valor)

  def desenfileirar(self):
    return self.lista.excluir_inicio()

  def fila_vazia(self):
    return self.lista.lista_vazia()

  def ver_inicio(self):
    if self.lista.primeiro == None:
      return -1
    return self.lista.primeiro.valor


fila = FilaListaEncadeada()
fila.enfileirar(20)
fila.enfileirar(40)
print(fila.ver_inicio())
print()

fila.enfileirar(50)
fila.enfileirar(10)
print(fila.ver_inicio())

fila.desenfileirar()
print(fila.ver_inicio())





