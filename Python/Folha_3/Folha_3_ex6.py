#Seja A uma matriz de m linhas e n colunas e X um vetor de dimensão N. Escreva um algoritmo para multiplicar uma matriz por um vetor.

#Imports
from modulo_acesso_ficheiros import*


#Defenir uma função
def transforma_linear(A,X):
    if len(A[0])==len(X):
        B=[[0]*len(X) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(X)):
                B[i][j]=A[i][j]*X[j]
        
        return B
    
    else:
        return False

#Testar a função
print("\t ----Matriz A----")
num_lines=int(input("Numero de linhas - "))
num_colums=int(input("Numero de colunas - "))
A=[]

for i in range(num_lines):
    Line=[]
    for j in range(num_colums):
        x=float(input("X["+str(i)+","+str(j)+"] - "))
        Line.append(x)

    A.append(Line)

print("\t ----Vetor X----")
N=int(input("Numero de componentes do vetor"))
X=[0]*N
for i in range(N):
    X[i]=float(input("x - "))

if transforma_linear(A,X)==False:
    print("Não é possivel realizar a operação")

else:
    print(transforma_linear(A,X))

