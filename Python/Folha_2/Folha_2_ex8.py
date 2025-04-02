#Escreva um algoritmo para calcular o elemento máximo de um vetor e respetiva posição. Defina a função max_pos(X) para implementar a resolução do algoritmo e um programa para testar a função.

def max_pos(N):
    X=[]

    for i in range(1,N+1):
        x=float(input("x - "))
        X.append(x)
    
    max=X[0]
    pos=1
    for i in range (0,N):
        if X[i]>max:
            max=X[i]
            pos=i+1
    
    return(max,pos)

num=int(input("Numero de componentes do vetor - "))
print(max_pos(num))
