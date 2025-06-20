# Criação do nó
class NoDuplo:
  def __init__(self, dado):
    self.dado = dado
    self.proximo = None
    self.anterior = None

# Criação da classe Lista Duplamente Encadeada
class ListaDuplamenteEncadeada:
  def __init__(self):
    self.cabeca = None

  def lista_vazia(self):
    return self.cabeca is None

  # Método inserir no inicio
  def inserirNoInicio(self, dado):
    novoNo = NoDuplo(dado)
    if self.lista_vazia():
      novoNo.proximo = novoNo.anterior = novoNo
      self.cabeca = novoNo
    else:
      cauda = self.cabeca.anterior
      novoNo.proximo = self.cabeca
      novoNo.anterior = cauda
      cauda.proximo = novoNo
      self.cabeca.anterior = novoNo
      self.cabeca = novoNo

  # Método inserir no fim
  def inserirNoFim(self, dado):
    if self.lista_vazia():
      self.inserirNoInicio(dado)
    else:
      cauda = self.cabeca.anterior
      novoNo = NoDuplo(dado)
      novoNo.proximo = self.cabeca
      novoNo.anterior = cauda
      cauda.proximo = novoNo
      self.cabeca.anterior = novoNo

  # Método para exibir
  def mostrar(self):
    if self.lista_vazia():
      print("Lista vazia.")
      return
    atual = self.cabeca
    while True:
      print(atual.dado, end=" <-> ")
      atual = atual.proximo
      if atual == self.cabeca:
        break
    print("(volta ao início)")

  # Método que insere em índice específico
  def inserirNoIndice(self, dado, indice):
    if indice < 0:
      print("Índice inválido! Por gentileza informar índice igual ou maior que zero.")
      return
    if indice == 0:
      self.inserirNoInicio(dado)
      return

    atual = self.cabeca
    for i in range(indice - 1):
      atual = atual.proximo
      if atual == self.cabeca:
        print("Índice inválido")
        return

    novoNo = NoDuplo(dado)
    proximoNo = atual.proximo
    novoNo.anterior = atual
    novoNo.proximo = proximoNo
    atual.proximo = novoNo
    proximoNo.anterior = novoNo

  # Método remover no início
  def removerNoInicio(self):
    if self.lista_vazia():
      print("A lista está vazia. Não é possível remover.")
      return

    if self.cabeca.proximo == self.cabeca:
      self.cabeca = None
    else:
      cauda = self.cabeca.anterior
      self.cabeca = self.cabeca.proximo
      self.cabeca.anterior = cauda
      cauda.proximo = self.cabeca

  # Método remover no fim
  def removerNoFim(self):
    if self.lista_vazia():
      print("A lista está vazia. Não é possível remover.")
      return

    if self.cabeca.proximo == self.cabeca:
      self.cabeca = None
    else:
      cauda = self.cabeca.anterior
      novaCauda = cauda.anterior
      novaCauda.proximo = self.cabeca
      self.cabeca.anterior = novaCauda

  # Método remover por índice
  def removerNoIndice(self, indice):
    if indice < 0:
      print("Índice inválido! Por gentileza informar índice igual ou maior que zero.")
      return
    if self.lista_vazia():
      print("A lista está vazia. Não é possível remover.")
      return
    if indice == 0:
      self.removerNoInicio()
      return

    atual = self.cabeca
    for i in range(indice):
      atual = atual.proximo
      if atual == self.cabeca:
        print("Índice fora dos limites.")
        return

    atual.anterior.proximo = atual.proximo
    atual.proximo.anterior = atual.anterior

# ---> TESTE DE CÓDIGO <--- #

# Métodos de inserção
print("\nMÉTODOS DE INSERÇÃO\n")
lista2 = ListaDuplamenteEncadeada()
lista2.inserirNoInicio(10)
lista2.inserirNoInicio(20)
lista2.mostrar()
lista2.inserirNoFim(30)
lista2.mostrar()
lista2.inserirNoIndice(15, 1)
lista2.mostrar()

# Métodos de exclusão
print("\nMÉTODOS DE EXCLUSÃO\n")
lista2.removerNoInicio()
lista2.mostrar()
lista2.removerNoFim()
lista2.mostrar()
lista2.inserirNoFim(25)
lista2.mostrar()
lista2.removerNoIndice(1)
lista2.mostrar()

# Métodos de borda da lista
print("\nMÉTODOS DE BORDA\n")
lista2.removerNoInicio()
lista2.removerNoInicio()
lista2.mostrar()
