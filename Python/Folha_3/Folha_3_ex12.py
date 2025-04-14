#Escrever um algoritmo e um programa para multiplicar duas matrizes. 

from modulo_acesso_ficheiros import*

#Defenir a função
def multiplicar_matrizes(A,B):
    if len(A[0])!=len(B):
        return False
    
    else:
        Y=[[0]*len(B[0]) for i in range(len(A))]
        for i in range(len(Y)):
            for j in range(len(Y[0])):
                x=0
                for k in range(len(Y[0])):
                    x+=A[i][k]*B[j][k]
                Y[i][j]=x
        
        return Y
    
#Testar a função
print("\t ----MATRIZ A----")
num_lines=int(input("Numero de linhas - "))
num_colums=int(input("Numero de colunas - "))
A=[]

for i in range(num_lines):
    Line=[]
    for j in range(num_colums):
        x=float(input("X["+str(i)+","+str(j)+"] - "))
        Line.append(x)

    A.append(Line)


print("\t ----MATRIZ B----")
num_lines=int(input("Numero de linhas - "))
num_colums=int(input("Numero de colunas - "))
B=[]

for i in range(num_lines):
    Line=[]
    for j in range(num_colums):
        x=float(input("X["+str(i)+","+str(j)+"] - "))
        Line.append(x)

    B.append(Line)


#Resultado
if multiplicar_matrizes(A,B)==False:
    print("Não é possível realizar a operação")

else:
    print(multiplicar_matrizes(A,B))