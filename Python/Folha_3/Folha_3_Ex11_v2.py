from modulo_acesso_ficheiros import*

def coluna_soma(X):

    for i in range(len(X)):
        sum=0
        for j in range(len(X[i])-1):
            sum+=X[i][j]
        
        X[i][len(X[i])-1]=sum
    
    return X
    
X=le_matriz_de_ficheiro_de_texto("matriz_A.txt")

print(coluna_soma(X))
