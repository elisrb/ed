
class No:
    def __init__(self, valor):
        self.__valor = valor
        self.__filhos = []

    def get_valor(self):
        return self.__valor

    def inserir_filhos(self, no):
        #pode self.__filhos pois o método faz parte do objeto (acesso interno)
        self.__filhos.append(No(no))

    def get_filhos(self):
        return [filho.get_valor() for filho in self.__filhos]
    
class Arvore:
    def __init__(self, valor):
        self.__raiz = No(valor)
    
    def get_raiz(self):
        return self.__raiz
    
    def conta_nos(self, no_pai=None):
        pass

    def get_altura(self, no_pai=None):
        pass

    def get_folhas(self, no_pai=None):
        pass 

    def imprimir_arvore(self, no=None, prefixo="", is_ultimo=True):
        
        if not no:
            no = self.__raiz

        # Imprime o prefixo
        print(prefixo, end="")

        # Verifica se é o último nó do nível
        if is_ultimo:
            print("`-- ", end="")
            prefixo += "    "
        else:
            print("|-- ", end="")
            prefixo += "|   "

        # Imprime o valor do nó atual
        print(no.get_valor())

        # Imprime os filhos recursivamente
        for i, filho in no.get_filhos():
            self.imprimir_arvore(filho, prefixo, i == len(no.get_filhos()) - 1)



'''arvore = Arvore(3)
n3 = arvore.get_raiz()

n1 = No(1)
n3.inserir_filhos(n1)

n1.inserir_filhos(No(5))
n1.inserir_filhos(No(10))
n1.inserir_filhos(No(7))
n1.inserir_filhos(No("Meu nome é Caetano"))

n4 = No(4)

arvore.imprimir_arvore(n1)

print(n1.get_filhos())

print('oi')'''

n1 = No(1)
print(n1.get_valor())
n1.inserir_filhos(2)
n1.inserir_filhos(3)
n1.inserir_filhos(4)
print(n1.get_filhos())