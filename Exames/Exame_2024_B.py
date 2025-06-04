'''Seja A uma matriz com m linhas e n colunas e X um vetor de dimensão N. Escreva uma função: 
 
a) Cria_vetor para definir o vetor Y da seguinte forma: o primeiro elemento é igual à média aritmética 
dos elementos da matriz inferiores a cinco, o segundo elemento é igual à média dos elementos 
superiores a cinco e por fim o produto dos elementos da penúltima coluna de A.  
 
b) Transforma_matriz para transformar a matriz A, trocando em cada linha o maior elemento pelo 
menor. 
 
c) Transforma_vetor para transformar o vetor X de inteiros, substituindo cada elemento pelo fatorial 
do elemento seguinte. 
(nota: não aplicar a função fatorial)'''

#Alinea A
def Cria_vetor(X):
    #Determinar as medias
    sum_inf_5=0
    cont_inf_5=0
    sum_sup_5=0
    cont_sup_5=0
    prod=1
    for i in range(len(X)):
        for j in range(len(X[i])):
            if X[i][j]<5:
                sum_inf_5+=X[i][j]
                cont_inf_5+=1
            
            elif X[i][j]>5:
                sum_sup_5+=X[i][j]
                cont_sup_5+=1
        #Determinra o pordutorio dos ultimos elementos da penultima coluna
        prod=prod*X[i][len(X[i])-2]
    
    Y=[sum_inf_5/cont_inf_5,sum_sup_5/cont_sup_5,prod]

    return Y

#Alinea B
def Transforma_matriz(A):
    for i in range(len(A)):
        max=A[i][0]
        id_max=0
        min=A[i][0]
        id_min=0
        #Determinar o elemento maximo e minimo da linha
        for j in range(1,len(A[i])):
            if A[i][j]>max:
                max=A[i][j]
                id_max=j
            
            if A[i][j]<min:
                min=A[i][j]
                id_min=j
        #Trocar os elementos
        A[i][id_min]=max
        A[i][id_max]=min

    return A

#Alinea C
def Transforma_vetor(X):
    for i in range(len(X)):
        #determinar o fatorial
        factorial=1
        for j in range(1,X[i]+1):
            factorial=factorial*j

        #Trocar o elemento do vetor pelo fatorial
        X[i]=factorial
    
    return X

'''Escreva uma função que determina qual é o maior elemento ímpar de um vetor de números inteiros. 
(sem recorrer à utilização de um vetor auxiliar).'''

def max_impar(X):
    id_max=0
    for i in range(len(X)):
        if X[i]%2!=0:
            max=X[i]
            id_max=i
            break
    
    for i in range(id_max,len(X)):
        if X[i]%2!=0:
            if X[i]>max:
                max=X[i]
                id_max=i
    
    return max,id_max
            

#testar as funções
from modulo_acesso_ficheiros import*
X=[1,5,2,9,4,10,1]
print(max_impar(X))
