# -- Identificando se uma lista encadeada está vazia

#Criação da classe Nodo

class Nodo:
    def __init__(self, codigo=0, proximo_nodo=None):
        self.codigo = codigo
        self.proximo = proximo_nodo # Corrigido para 'proximo_nodo'

    def __repr__(self):
        return '%s -> %s' % (self.codigo, self.proximo)
    
#Criação da classe Lista Encadeada    

class Lista_Encadeada:
    def __init__(self):
        self.cabeca = None
    
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    
#Criação da função que verifica a lista

def verifica_vazia(Lista):
    print("***VERIFICA LISTA VAZIA*** \nA lista está vazia? ")
    if Lista.cabeca == None:
        print("True")
    else:
        print("False")

#Código principal

Lista = Lista_Encadeada()
verifica_vazia(Lista)

#Acessando o primeiro item da lista (que retorna None porque está vazia)

Primeiro = Lista.cabeca
print("\n***VERIFICA PRIMEIRO ITEM DA LISTA***\n", Primeiro)