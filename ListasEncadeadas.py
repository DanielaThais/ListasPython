# Esta classe representa um nó (ou nodo) de uma lista encadeada.
class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None): 
        self.dado = dado
        self.proximo = proximo_nodo 

    def __repr__(self):
        # Define como um objeto NodoLista é representado como string.
        # Isso é crucial para que o __repr__ da ListaEncadeada funcione corretamente.
        return f"{self.dado} -> {self.proximo}" if self.proximo else f"{self.dado}"

# Esta classe representa uma lista encadeada.   
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        if self.cabeca is None:
            return "[]"  # Retorna "[]" se a lista estiver vazia
        
        # Percorre a lista para construir a representação em string de todos os elementos
        atual = self.cabeca
        elementos = []
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return "[" + " -> ".join(elementos) + "]"

# Esta função é responsável pela inserção do primeiro elemento da lista.
def insere_no_inicio(lista, novo_dado):
    # 1) Cria um novo nó com o dado a ser armazenado.
    novo_nodo = NodoLista(novo_dado)

    # 2) Faz com que o novo nó aponte para a cabeça atual da lista.
    novo_nodo.proximo = lista.cabeca

    # 3) Faz com que a cabeça da lista referencie o novo nó, tornando-o o primeiro.
    lista.cabeca = novo_nodo


# --- Verificar o funcionamento adequado das classes criadas ---

lista = ListaEncadeada()
print("Lista vazia: ", lista)

insere_no_inicio(lista, 5)
print("Lista contém um único elemento: ", lista)

insere_no_inicio(lista, 10)
print("Lista com dois elementos: ", lista) # Adicionei esta linha para ver o resultado da segunda inserção

insere_no_inicio(lista, 20)
print("Lista com três elementos: ", lista)

