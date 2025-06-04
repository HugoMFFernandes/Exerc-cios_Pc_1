'''Seja A uma matriz com m linhas e n colunas. Escreva uma função em Python que cria o vetor B com 
os elementos pares da primeira coluna de A, acrescentando o elemento máximo da última linha da 
matriz. '''

def criar_vetor(A):
    B=[]
    #Elementos pares da primeira coluna
    for i in range(len(A)):
        if A[i][0]%2==0:
            B.append(A[i][0])
    
    #Elemento maximo da ultima coluna
    max=A[len(A)-1][0]
    id_max_j=0
    for j in range(1,len(A[len(A)-1])):
        if A[len(A)-1][j]>max:
            max=A[len(A)-1][j]
            id_max_j=j
    
    B.append(A[len(A)-1][id_max_j])

    return B

'''Seja A um vetor de números naturais de dimensão n e k um número natural dado. 
a) Escreva uma função que define um vetor com os primeiros k termos da sequência de Fibonacci 
que são múltiplos de 3. 
b) Escreva uma função que determina qual é o elemento do vetor A que tem mais divisores. 
Neste exercício deve testar a função da alínea b) com o vetor resultado da alínea a).'''


#Alinea A
def vetor_fibonacci(k):
    if k<3:
        return False
    
    if k>=3:
        X=[3]
        sequencia=[1,2,3]
        while len(sequencia)<k:
            sequencia.append(sequencia[len(sequencia)-2]+sequencia[len(sequencia)-1])
        
        for i in range(3,len(sequencia)):
            if sequencia[i]%3==0:
                X.append(sequencia[i])
    
    return X



#Alinea B
def mais_divisores(X):
    #Criar o vetor numero de divisores
    cont_div=[1]*len(X)

    for i in range(len(X)):
        if X[i]==1:
            cont_div[i]=1

        elif X[i]==2:
            cont_div[i]=2    

        else:
            for j in range(2,(X[i]//2)+1):
                if X[i]%j==0:
                    cont_div[i]+=1
    
    #Encontrar o elemento como maior numerom de divisores
    max=cont_div[0]
    id_max=[]
    #Encontrar o valor maximo de divisores
    for i in range(1,len(X)):
        if cont_div[i]>max:
            max=cont_div[i]

    for i in range(len(cont_div)):
        if cont_div[i]==max:
            id_max.append(i)
    
    return id_max

#Testar as funções
k=40
resultado=vetor_fibonacci(k)
print(resultado)
print(mais_divisores(resultado))
            