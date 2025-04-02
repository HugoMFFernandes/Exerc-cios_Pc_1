#Escreva um algoritmo para transformar um vetor trocando o elemento máximo pelo elemento mínimo. 
#a) Escreva a função troca_max_min(X) para trocar o elemento máximo do vetor X com o elemento mínimo. 
#b) Escrever um programa para testar a função troca_max_min(X).

def troca_max_min(N):
    
    #Determinar o vetor
    X=[]
    for i in range(1,N+1):
        x=float(input("x - "))
        X.append(x)
    
    #Determninar o minimo e a sua posição 
    min=X[0]
    pos_min=0
    for i in range(1,N):
        if X[i]<min:
            min=X[i]
            pos_min=i

    #Determinar o maximo e a sua posição
    max=X[0]
    pos_max=0
    for i in range(1,N):
        if X[i]>max:
            max=X[i]
            pos_max=i
    
    #Trocar o valor máximo com o valor minimo
    aux=X[pos_max]
    X[pos_max]=X[pos_min]
    X[pos_min]=aux

    return X

num=int(input("Numero de componentes do vetor - "))
print(troca_max_min(num))