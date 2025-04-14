# Escreva um algoritmo para definir uma matriz A de ordem N triangular inferior em que todos os elementos abaixo da diagonal principal são iguais a valor_1 e na diagonal principal valor_2.

def define_mat_TriangInferior(A,valor_1,valor_2):
    for i in range(1,len(A[0])):
        A[0][i]=valor_2
    
    for i in range(1,len(A)):
        for j in range(i):
            A[i][j]=valor_1
        
        for j in range(i+1,len(A[i])):
            A[i][j]=valor_2
    
    return A

N=int(input("Numero de linhas/colunas da matriz - "))
A=[[0]*N for i in range(N)]
for i in range(N):
    A[i][i]=float(input("A["+str(i)+","+str(i)+"] - "))

valor_1=float(input("Valor_1 - "))
valor_2=float(input("valor_2 - "))

print(define_mat_TriangInferior(A,valor_1,valor_2))