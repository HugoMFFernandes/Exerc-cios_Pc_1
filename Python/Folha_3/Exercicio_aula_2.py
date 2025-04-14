import random
from modulo_acesso_ficheiros import*


def construir_matriz(N,M):
    X=[[0]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            X[i][j]=random.randint(10,100)
    
    return X
            
N=int(input("Numero de linhas - "))
M=int(input("Numero de colunas - "))

X=construir_matriz(N,M)

print(X)
escreve_matriz_ficheiro("matriz_X.txt",X)