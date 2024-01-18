total = int(input())
letras = 'QWERTYUIOPASDFGHJKLZXCVBNM'
i = 0
while i < total:
    linha = input()
    indice = 0
    string = ''
    numero = ''
    nao_acabou = True
    while nao_acabou:
        letra = linha[indice]
        numero = ''
        for termo in linha[indice+1:]:
            if termo not in letras:
                indice+=1
                numero += termo
                if indice+1 == len(linha):
                    nao_acabou = False
            else:
                indice = linha.index(termo)
                break
        string += letra*int(numero)
    print(string)
    i+=1