from modulo_acesso_ficheiros import*
from random import*

'''Seja A uma matriz com m linhas e n colunas e X um vetor de dimensão N. Escreva uma função: 
 
a) Cria_vetor para definir o vetor Y da seguinte forma: o primeiro elemento é igual à média aritmética 
dos elementos da matriz inferiores a cinco, o segundo elemento é igual à média dos elementos 
superiores a cinco e por fim o produto dos elementos da penúltima coluna de A. 
'''

def Cria_vetor(A):
    X=[0]*3
    sum_inf_5=0
    cont_inf_5=0
    sum_sup_5=0
    cont_sup_5=0
    for i in range(len(A)):
        for j in range((len(A[0]))):
            #Soma dos elementos inferiores a 5
            if A[i][j]<5:
                sum_inf_5+=A[i][j]
                cont_inf_5+=1
            #Soma dos elementos superiores a 5
            elif A[i][j]>5:
                sum_sup_5+=A[i][j]
                cont_sup_5+=1

    if cont_inf_5==0:
        X[0]="Não existem elementos na matriz que sejam inferiores a 5"
    
    else:
        X[0]=sum_inf_5/cont_inf_5
    
    if cont_sup_5==0:
        X[1]="Não existem elementos na matriz que sejam superiores a 5"
    
    else:
        X[1]=sum_sup_5/cont_sup_5

    #Produtorio dos elementos da penultima coluna
    produtorio=1
    for i in range(len(A)):
        produtorio*=A[i][len(A)-2]
    
    X[2]=produtorio

    return X
''' 
b) Transforma_matriz para transformar a matriz A, trocando em cada linha o maior elemento pelo 
menor. 
'''

def Transforma_matriz(A):
    for i in range(len(A)):
        max=A[i][0]
        min=A[i][0]
        id_max=[]
        id_min=[]
        #Encontrar o maximo e o minimo
        for j in range(1,len(A[0])):
            if A[i][j]>max:
                max=A[i][j]
            
            elif A[i][j]<min:
                min=A[i][j]
    
        #Encontrar a posição dos elementos maximos e minimos
        for j in range(len(A[i])):
            if A[i][j]==max:
                id_max.append(j)
            elif A[i][j]==min:
                id_min.append(j)
        
        #Trocar elementos
        for k in range(len(id_max)):
            A[i][id_max[k]]=min
        
        for k in range(len(id_min)):
            A[i][id_min[k]]=max
    
    return A

def Transfoma_matriz_v2(A):
    
    for i in range(len(A)):
        max=A[i][0]
        id_max=[0]
        min=A[i][0]
        id_min=[0]
        for j in range(1,len(A[i])):
            #Determinar os maximos e as suas posições
            if A[i][j]>max:
                max=A[i][j]
                id_max=[j]
            
            elif A[i][j]==max:
                id_max.append(j)
            
            #Determinar os minimos e as suas posições
            if A[i][j]<min:
                min=A[i][j]
                id_min=[j]
            
            elif A[i][j]==min:
                id_min.append(j)
        
        #Trocar os elementos
        for j in range(len(id_max)):
            A[i][id_max[j]]=min

        for j in range(len(id_min)):
            A[i][id_min[j]]=max
        
    return A




X=[[3, -2, -10, -3, -8], [9, 7, 9, -4, 0], [4, -5, -2, 6, -4], [7, -3, -8, 8, 7], [-6, 3, -6, -8, 8]]
Resultado=Transfoma_matriz_v2(X)
for i in range(len(X)):
    print(Resultado[i])



'''
c) Transforma_vetor para transformar o vetor X de inteiros, substituindo cada elemento pelo fatorial 
do elemento seguinte. 
(nota: não aplicar a função fatorial)'''

def Transforma_vetor(X):
    Y=[0]*len(X)
    #Fatorial do elemento 0 até len(X)-1
    for i in range(len(X)-1):
        factorial=1
        for j in range(1,X[i+1]+1):
            factorial*=j
        Y[i]=factorial
    
    #Fatoerial elemento len(X)
    factorial=1
    for j in range(1,X[0]+1):
        factorial*=j
    Y[len(X)-1]=factorial
    
    return Y

'''Escreva uma função que determina qual é o maior elemento ímpar de um vetor de números inteiros. 
(sem recorrer à utilização de um vetor auxiliar).'''

def max_impar(X):
    #Determinar o valor máximo inicial
    i=0
    while i<len(X) and X[i]%2==0:
        i+=1
        if X[i]%2!=0:
            max=X[i]
    if i==len(X):
        return "Não existem numeros impares"
    else:
        max=X[i]
        id_max=[i]
        for i in range(i+1,len(X)):
            if X[i]%2!=0:
                if X[i]>max:
                    max=X[i]
                    id_max=[i]
                elif X[i]==max:
                    id_max.append(i)
        
        return "Valor máximo -",max,"Posição dos valores máximos -",id_max

N=int(input("N - "))
Y=[0]*N
for i in range(N):
    Y[i]=randint(0,100)
print(Y)
print(max_impar(Y))

