#Soma de duas matrizes

#Função soma de matrizes
def soma_matrizes(A,B):
    X=[[0]*len(X[0]) for i in range(len(A))]
    if len(A)!=len(B) or len(A[0])!=len(B[0]):
        return False

    else:
        X=[[0]*len(X[0]) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[i])):
                X[i][j]=A[i][j]+B[i][j]
        
        return X

#Testar a função
print("\t ---Matriz A---")

N=int(input("Numero de linhas de A - "))
M=int(input("Numero de colunas de A - "))
A=[[0]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        A[i][j]=float(input("x - "))


print("\t ---Matriz B---")

N=int(input("Numero de linhas de B - "))
M=int(input("Numero de colunas de B - "))
B=[[0]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        B[i][j]=float(input("x - "))

if soma_matrizes(A,B)==False:
    print("Não é possivel realizar a operação")

else:
    print(soma_matrizes(A,B))