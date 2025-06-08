#As mercadorias são cadastradas conforme seu tipo:
#Código 0 = produtos enlatados
#Código 1 = produtos refrigerados
#Os veículos suportam 50 caixas desses produtos, mas são listados no sistema sem classificação

#*****CRIAÇÃO DAS CLASSES****

class Produto:
    def __init__(self,Codigo="indefinido", Peso=0):
        self.Codigo = Codigo
        self.Tipo = Peso

    def __repr__(self):
        return '%s -> %d'% (self.Codigo, self.Tipo)
    
#*****CLASSE NODO*****

class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.conteudo = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> $s'% (self.conteudo, self.proximo)
    
#*****CLASSE LISTA ENCADEADA*****

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
    
    def __repr__(self):
        return "[" +str(self.inicio) +"]"
    
    def ListaVazia(self):
        if self.inicio ==None:
            return True
        else:
            return False
    
    def ImprimeLista(self):
        atual = self.inicio
        cont = 0
        print("INÍCIO DA LISTA\n")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            while atual!=None:
                print("Posição: ", cont, atual)
                cont = cont +1
                atual = atual.proximo
        print("\nFinal da lista...")

    def TotalProdutoRefrigerado(self):
        atual = self.inicio
        total = 0

        if self.inicio == None:
            return 0
        while atual!= None:
            if(atual.Tipo ==1):
                total = total +1
            atual = atual.proximo
        return total
    
    def NovoProduto(self, Nd):
        atual= self.inicio
        Nd.proximo = atual
        self.inicio=Nd

lista = ListaEncadeada()

lista.NovoProduto(Produto("001", 1))
lista.NovoProduto(Produto("002", 0))
lista.NovoProduto(Produto("003", 1))
lista.NovoProduto(Produto("004", 0))
lista.NovoProduto(Produto("005", 0))

lista.ImprimeLista()
print("\nTotal de produtos com Refrigeração: ", lista.TotalProdutoRefrigerado())
    
