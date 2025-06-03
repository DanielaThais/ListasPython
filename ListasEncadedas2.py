# -- PESQUISANDO ELEMENTO DENTRO DA LISTA

#definindo classe de Lista Encadeada

class ListaEncadeada:
    def __init__(self):
        self.inicio = None #Assume que o 'início' é a cabeça da lista

#Método 1 - função que retorna se achou um elemento em uma lista

def ExisteNodo(self, item):
    atual = self.inicio
    while atual is not None: 
        if atual.inf() == item:
            return True
       
        atual = atual.proxNodo()     
    
    return False

class Nodo:
    def __init__(self, dado, proximo = None):
        self.dado = dado
        self.proximo = proximo

    #Método para obter o dado
    def inf(self)
        return self.dado

    #Método para obter o próximo nó
    def proxNodo(self)
        return self.proximo

class SegundaListaEncadeada:
    def __init__(self):
        self.inicio = None

    def existe_nodo(self, item): 
        atual = self.inicio
        while atual is not None: 
            if atual.inf() == item:
                return True
        
            atual = atual.proxNodo()     
        
        return False

# -- INCLUINDO ELEMENTOS NA LISTA

def inserir (self, item, pos):
    atual = self.inicio
    pos_atual = 0

    while atual.proximo != None:
        if pos_atual == (pos-1):
            pointer = atual
            node = Nodo(item)
            node.proximo = pointer.proximo
            pointer.proximo = node

        else:
            atual = atual.proximo

    pos_atual = pos_atual + 1

#Método 2

lista = [1, 2, 3, 4]
lista.insert (2, 10)
print (lista)


#verificar se estão ok.