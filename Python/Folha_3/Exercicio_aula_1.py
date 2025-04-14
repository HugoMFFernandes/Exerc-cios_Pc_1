from modulo_acesso_ficheiros import*

def vetor_neg(X):
    Y=[]
    for i in range(len(X)):
        for j in range(len(X[i])):
            if X[i][j]<0:
                Y.append(X[i][j])
    
    if len(Y)==0:
        return False

    else:
        return(Y)


X=le_matriz_de_ficheiro_de_texto("matriz_A.txt")
if vetor_neg(X)==False:
    print("A matriz não tem valores negativos")

else:
    print(vetor_neg(X))