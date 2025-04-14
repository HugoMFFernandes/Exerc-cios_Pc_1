#Exercicio 1.b)
def m_matriz_escalar(A,k):
    B=[[0]*len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j]=A[i][j]*k
            B.append(A[i][j])
    
    return B

def m_matriz_dp(X):
    produtorio=1
    for i in range(len(X)):
            produtorio=produtorio*X[i][i]
        
    return produtorio
    
    

def m_matriz_ds(X):
    
    produtorio=1
    for i in range(len(X)):
            produtorio=produtorio*X[i][len(X)-1-i]
        
    return produtorio
    
    