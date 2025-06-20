# Criação do nó da lista
class No:
  def __init__(self, valorInicial):
    self.valor = valorInicial;
    self.proximo = None;

# Criação da classe de lista simplesmente encadeada
class ListaSimplesmenteEncadeada:
  def __init__(self):
    self.inicio = None

# Método para inserir início da lista
  def inserir_no_inicio(self, valor):
    NovoNo = No(valor)
    NovoNo.proximo = self.inicio
    self.inicio = NovoNo

# Método para imprimir resultado
  def mostrar(self):
    atual = self.inicio
    while atual:
      print(atual.valor, end=" -> ") #OBS: Incluí a seta no final, pois facilita a leitura
      atual = atual.proximo
    print("Fim")

# Verificando o tamanho da lista
  def tamanho(self):
    tamanho = 0 #contator
    atual = self.inicio
    while atual:
      tamanho += 1 #incrementa o tamanho
      atual = atual.proximo
    print ("A quantidade de elementos da lista é: " + str(tamanho))


# Método pesquisar
  def pesquisar(self, valorPesquisa):
    atual = self.inicio
    indice = 0
    while atual:
      if atual.valor == valorPesquisa:
        return indice
      atual = atual.proximo
      indice += 1
    return -1

# Método de exclusão de dado
  def excluir_dado(self, valor):
    atual = self.inicio
    anterior = None

    while atual:
      if atual.valor == valor:
        if anterior is None:
          self.inicio = atual.proximo
        else:
          anterior.proximo = atual.proximo
        print(f"O valor {valor} foi excluído da lista.")
        return
      anterior = atual
      atual = atual.proximo

    print(f"O valor {valor} não foi encontrado na lista.")

# Método excluir em determinado índice
  def excluir_no_indice(self, indice):
    if indice < 0:
      print("Índice inválido! Por gentileza informar índice igual ou maior que zero.")
      return

    atual = self.inicio
    anterior = None
    atual_indice = 0

    while atual:
      if atual_indice == indice:
        if anterior is None:
          # remove o primeiro nó
          self.inicio = atual.proximo
        else:
          #remove do meio para o final
          anterior.proximo = atual.proximo
        print(f"O número no índice {indice} foi excluído da lista.")
        return
      anterior = atual
      atual = atual.proximo
      atual_indice += 1

# Método que insere em índice específico
  def inserir_no_indice(self, indice, valor):
    if indice < 0:
      print("Índice inválido! Por gentileza informar índice igual ou maior que zero.")
      return

    novo_no = No(valor)

    if indice == 0:
      novo_no.proximo = self.inicio
      self.inicio = novo_no
      print(f"O número {valor} foi inserido no índice {indice} da lista.")
      return

    atual = self.inicio
    atual_indice = 0

    while atual and atual_indice < indice - 1:
      atual = atual.proximo
      atual_indice += 1

    if atual is None:
      print(f"Índice fora dos limites da lista! A lista possui apenas {atual_indice} elementos.")
      return

    novo_no.proximo = atual.proximo
    atual.proximo = novo_no
    print(f"O número {valor} foi inserido no índice {indice} da lista.")

# ---> TESTE DE CÓDIGO <--- #

lista1 = ListaSimplesmenteEncadeada()
lista1.inserir_no_inicio(10)
lista1.inserir_no_inicio(20)
lista1.inserir_no_inicio(30)
lista1.inserir_no_inicio(40)
lista1.mostrar()
lista1.tamanho()

# PESQUISA NÚMERO

resultado1 = lista1.pesquisar(40)
if resultado1 != -1:
  print(f"O número 40 foi encontrado no índice {resultado1}")
else:
  print("Número 40: não encontrado!")
resultado2 = lista1.pesquisar(50)
if resultado2 != -1:
  print(f"O número 50 foi encontrado no índice {resultado2}")
else:
  print("Número 50: não encontrado!")

# MÉTODOS DE EXCLUSÃO DE DADOS

print("\nMÉTODO EXCLUI DADO\n")
lista1.mostrar();
lista1.excluir_dado(20);
lista1.mostrar();
print("\nMÉTODO EXCLUI DADO NO ÍNDICE\n")
lista1.excluir_no_indice(0);

# MÉTODO INSERE NO ÍNDICE

print("\nMÉTODO INSERE NO ÍNDICE\n")
lista1.inserir_no_indice(50, 0);
lista1.inserir_no_indice(60, 3);
lista1.mostrar();
