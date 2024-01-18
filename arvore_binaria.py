
class NoArvoreBB():
    def __init__(self, dado, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

# insere é um função
def insere(raiz, no):
    if not raiz:
        return no
    
    if no.dado < raiz.dado:
        raiz.esq = insere(raiz.esq, no)
    else:
        raiz.dir = insere(raiz.dir, no)

    return raiz

def preorder(raiz):
    if raiz:
        print(raiz.dado)
        preorder(raiz.esq)
        preorder(raiz.dir)

def inorder(raiz):
    if raiz:
        inorder(raiz.esq)
        print(raiz.dado)
        inorder(raiz.dir)

def posorder(raiz):
    if raiz:
        posorder(raiz.esq)
        posorder(raiz.dir)
        print(raiz.dado)

def busca_largura(raiz, dado):
    fila = [raiz]
    while len(fila) > 0:
        if fila[0].dado == dado:
            return True
        if fila[0].esq:
            fila.append(fila[0].esq)
        if fila[0].dir:
            fila.append(fila[0].dir)
        print([x.dado for x in fila]) #teste
        fila.pop(0)
    return False

def busca_profundidade(raiz, dado, pilha = []): #?????
    if raiz:
        if len(pilha) == 0:
            pilha.append(raiz)
        if raiz.dado == dado:
            return True
        if raiz.esq:
            pilha.append(raiz.esq)
        if raiz.dir:
            pilha.append(raiz.dir)
        print([x.dado for x in pilha]) #teste
        pilha.pop()
        if len(pilha) > 0:
            busca_profundidade(pilha[-1], dado, pilha)
        return False

#testes
raiz = NoArvoreBB(50)
raiz = insere(raiz, NoArvoreBB(17))
raiz = insere(raiz, NoArvoreBB(72))
raiz = insere(raiz, NoArvoreBB(12))
raiz = insere(raiz, NoArvoreBB(23))
raiz = insere(raiz, NoArvoreBB(54))
raiz = insere(raiz, NoArvoreBB(76))
raiz = insere(raiz, NoArvoreBB(9))
raiz = insere(raiz, NoArvoreBB(14))
raiz = insere(raiz, NoArvoreBB(19))
raiz = insere(raiz, NoArvoreBB(67))

print(f"preorder")
preorder(raiz)
print(f"inorder")
inorder(raiz)
print(f"posorder")
posorder(raiz)

#print(busca_profundidade(raiz, 10))
print(busca_largura(raiz, 10))

print('iu')

'''def busca_largura_rec(raiz, dado, fila=[]):
    if raiz:
        if len(fila) == 0:
            fila.append(raiz)
        if raiz.dado == dado:
            return True
        if raiz.esq:
            fila.append(raiz.esq)
        if raiz.dir:
            fila.append(raiz.dir)
        #print([x.dado for x in fila]) #teste
        fila.pop(0)
        if len(fila) > 0:
            busca_largura_rec(fila[0], dado)
        return False'''