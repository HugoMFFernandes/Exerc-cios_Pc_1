'''Seja A um vetor de números naturais de dimensão n.  
a) Escreva uma função que calcula o fatorial de um número inteiro positivo. 
b) Escreva uma função que cria o vetor B com todos os elementos de A que são inferiores a 10, seguidos 
dos elementos que são múltiplos de 11 e por fim o fatorial do penúltimo elemento de A. '''

#Alinea A
def fatorial(N):
    fatorial=1
    for i in range(1,N+1):
        fatorial*=i
    
    return fatorial

#Alinea B
def criar_vetor_1(A):
    B=[]
    #Elementos inferiores a 10
    for i in range(len(A)):
        if A[i]<10:
            B.append(A[i])
    #Elementos multiplos de 11
    for i in range(len(A)):
        if A[i]%11==0:
            B.append(A[i])
    #Fatorial do penultimo elemento de A
    B.append(fatorial(A[len(A)-2]))

    return B


'''Seja A uma matriz de m linhas e n colunas.  
a) Escreva uma função que cria o vetor B colocando à esquerda as médias aritméticas das linhas da 
matriz, seguidos do produto dos elementos de cada coluna e por fim o elemento máximo da última 
coluna de A. 
 
 
a) Seja C um vetor de dimensão n. Escreva uma função que substitui o primeiro elemento positivo e ímpar 
do vetor pelo seu fatorial.'''

#Alinea A
def criar_vetor_2(A):
    B=[]
    #Media aritmetrica das linhas da matriz
    for i in range(len(A)):
        sum_line=0
        for j in range(len(A[i])):
            sum_line+=A[i][j]
        B.append(sum_line)
    
    #Produtorio das colunas
    for j in range(len(A[0])):
        prod=1
        for i in range(len(A)):
            prod*=A[i][j]
        B.append(prod)
    
    #Elemento maximo da ultima coluna
    max=A[0][len(A[0])-1]
    for i in range(1,len(A)):
        if A[i][len(A[0])-1]>max:
            max=A[i][len(A[0])-1]
    
    B.append(max)

    return B

#Alinea B
def trocar_vetor(C):
    cond=0
    id=0
    while cond==0:
        for i in range(len(C)):
            if C[i]>0 and C[i]%2!=0:
                cond=i
                id=i
    
    C[id]=fatorial(C[id])

    return C

