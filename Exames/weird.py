'''EXERCÍCIO 1
Seja A um vetor de números inteiros positivos:
a) Escreva uma função que calcula a soma de todos os números primos no vetor A.
b) Escreva uma função que cria um vetor B contendo todos os números de A divididos por 2,
seguidos do quadrado do maior número no vetor A.'''

#Alinea A
def soma_primos(A):
    sum=0
    for i in range(len(A)):
        if A[i]==2 or A[i]==3:
            sum+=A[i]
        
        else:
            cont=0
            for j in range(2,A[i]//2+1):
                if A[i]%j==0:
                    cont+=1
            
            if cont==0:
                sum+=A[i]
    
    return sum

#Alinea B
def criar_vetor(A):
    B=[A[i]/2 for i in range(len(A))]

    #Encontrar o maior elemento de A
    max=A[0]
    for i in range(1,len(A)):
        if A[i]>max:
            max=A[i]
    
    B.append(max**2)

'''
EXERCÍCIO 2
Seja M uma matriz de números inteiros de dimensões m x n:
a) Escreva uma função que cria um vetor contendo a soma de cada linha da matriz M.
b) Escreva uma função que substitui o maior elemento par da matriz M pelo seu valor triplicado.
'''
#Alinea A
def criar_vetor_soma_linha(M):
    X=[0]*len(M)
    for i in range(len(M)):
        sum_line=0
        for j in range(len(M[i])):
            sum_line+=M[i][j]
        X[i]=sum_line

    return X

#Alinea B
def trocar_matriz(M):
    max=None
    id_max=[]
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]%2==0:
                if max is None or M[i][j]>max:
                    max=M[i][j]

    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]==max:
                M[i][j]=3*M[i][j]
    if max is None:
        return 'Não existem numeros pares na matriz'
    
    else:
        return M


'''
EXERCÍCIO 3
Seja C um vetor de números inteiros:
a) Escreva uma função que encontra o menor número do vetor C e calcula o seu cubo.
b) Escreva uma função que cria um novo vetor contendo os elementos de C em ordem decrescente,
 seguidos pelo cubo do menor número.
'''

#Alinea A
def cubo_min(C):
    min=C[0]
    for i in range(1,len(C)):
        if C[i]<min:
            min=C[i]
    
    return min**3

#Alinea B
def vetor_decrescente(C):
    X=[]
    for i in range(len(C)):
        min=None
        id_min=0
        for i in range(len(C)):
            if min is None or C[i]<min:
                min=C[i]
    
        X.append(min)
        C.remove(min)
    
    return X




#Testar as funções
from modulo_acesso_ficheiros import*
X=le_matriz_de_ficheiro_de_texto("matriz_X.txt")
C=[5,6,8,-10]
print(vetor_decrescente(C))