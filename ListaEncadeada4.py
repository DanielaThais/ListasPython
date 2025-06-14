class No:
    #Constructor da classe No
    def __init__(self, dado_inicial):
        self.dado = dado_inicial#self recebe dado
        self.proximo = None #proximo recebe vazio para ligarmos o nó posteriormente

    #Gets e Sets
    def obtem_dado(self): #obtendo os dados do nó
        return (self.dado) #método obtem_dado recebe dado.

    def set_data(self, novo_dado): #set_data grava novo dado do nó
        self.dado = novo_dado

    def set_proximo(self, novo_proximo): #set_proximo grava o próximo nó
        self.proximo = novo_proximo

    def obtem_proximo_dado(self): 
        return (self.proximo) 

#Criando os nós
no1 = No(10) 
no2 = No(20) 

#Ligando os nós

no1.set_proximo(no2) #no1 aponta para no2

## VERIFICANDO SE A LISTA ESTÁ VAZIA

def lista_esta_vazia(no):
    if no == None:
        print("A lista está vazia")
        return True
    
    else:
        print("\nIMPRIME DADOS RECEBIDOS NOS NÓS: ")
        print("No1:", no1.obtem_dado()) #Imprime o dado do nó 1
        if no.obtem_proximo_dado() is not None:
            print ("No2: ", no.obtem_proximo_dado().obtem_dado())
        else:
            print("No2: None")
        print (">>>A lista NÃO está vazia<<<")
        return False
        
lista_esta_vazia(no1) #Chama a função para verificar se a lista está vazia
#Imprimindo o dado do nó 1 e o próximo nót