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
            
    
    B.append(max)

    return B

'''Seja A um vetor de números naturais de dimensão n e k um número natural dado. 
a) Escreva uma função que define um vetor com os primeiros k termos da sequência de Fibonacci 
que são múltiplos de 3. 
b) Escreva uma função que determina qual é o elemento do vetor A que tem mais divisores. 
Neste exercício deve testar a função da alínea b) com o vetor resultado da alínea a).'''


#Alinea A
def vetor_fibonacci(k):
    seq_fibonacci=[0,1,1,2]
    for i in range(k-4):
        seq_fibonacci.append(seq_fibonacci[len(seq_fibonacci)-2]+seq_fibonacci[len(seq_fibonacci)-1])
    
    X=[]
    for i in range(2,len(seq_fibonacci)):
        if seq_fibonacci[i]%3==0:
            X.append(seq_fibonacci[i])

    return seq_fibonacci,X

def caralhos(k):
    seq=[0,1,1]
    X=[]
    while len(seq)!=k:
        x=seq[len(seq)-2]+seq[len(seq)-1]
        seq.append(x)
        if x%3==0:
            X.append(x)
    
    return seq,X


#Alinea B
def maior_divisores(X):
    num_div=[2]*len(X)
    for i in range(len)
    for i in range(2,len(num_div)/2+1):
        cont=0
        if X[i]%i

    




#Testar as funções
k=10
print(caralhos(k))



