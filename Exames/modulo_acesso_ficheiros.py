# modulo_acesso_ficheiros
# Janeiro 2022: Luisa Sousa e Cristina Guedes
# Versao Preliminar para apoio as aulas de PC1
# le vetor a partir de um ficheiro de texto
def ler_vetor_coluna_ficheiro_de_texto(fich):
    f = open(fich, 'r') 
    y=[]
    x = f.readline()
    while x:
        y.append(float(x))
        x = f.readline()
        if x == "\n":
           print( "fim de linha....")
           break
    f.close()
    return y
#Fim
def ler_vetor_linha_ficheiro_de_texto(fich):
# l� vetores (em linha) a partir de um ficheiro de texto
    f = open(fich, 'r')   
    y=[]
    x = f.readline()
    y=x.split()
    for i in range(len(y)):
        y[i]=float(y[i])
    f.close()
    return y
#Fim

def escrever_vetor_linha_ficheiro_de_texto(fich,x):
# escreve vetor em linha para ficheiro de texto
    f = open(fich, 'w')
    for i in range(len(x)):
         f.write(str(x[i])+ ' ')     
    f.close()
#Fim    
def escrever_vetor_coluna_ficheiro_de_texto(fich,x):
# escreve vetores em ficheiro de texto
    f = open(fich, 'w')
    for i in range(len(x)):
         f.write(str(x[i])+'\n')     # '\n? cria uma nova linha
    f.close()
#Fim

#le_matriz_de_ficheiro_de_texto
def le_matriz_de_ficheiro_de_texto(fich):
    #fich: nome do ficheiro
    f = open(fich, "r")
    A = []
    while True: # repetir
        linha = f.readline() # uma nova linha
        if linha == "": # fim do ficheiro?
            break
        linha = linha.strip('\n')
        linha = linha.split()
        nlinha = []
        for j in range(len(linha)):
            list.append(nlinha,float(linha[j][:]))
        list.append(A,nlinha)
    f.close()
    return A
#Fim

def escreve_matriz_ficheiro(fich,A):
#fich: nome do ficheiro para guardar a matriz A
    f = open(fich, "w")
    nl = len(A)
    nc=len(A[0])
    
    for i in range(nl):
        nline=""
        for j in range(nc):
           nline= nline + str(A[i][j]) + "  "  # alterei espaços e corrigi nline
        f.write(nline)
        f.write('\n')
    f.close()
#FIM