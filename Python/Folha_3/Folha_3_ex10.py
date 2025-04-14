#Seja A uma matriz (m x n). Escrever um algoritmo para transformar a matriz A trocando a primeira coluna com a última. 

from modulo_acesso_ficheiros import*

#Defenir uma função
def trocar_coluna(A):
    for i in range(len(A)):
        aux=A[i][0]
        A[i][0]=A[i][len(A[i])-1]
        A[i][len(A[i])-1]=aux
    
    return A

#Testar a função
print("\t ----MATRIZ----")
num_lines=int(input("Numero de linhas - "))
num_colums=int(input("Numero de colunas - "))
X=[]

for i in range(num_lines):
    Line=[]
    for j in range(num_colums):
        x=float(input("X["+str(i)+","+str(j)+"] - "))
        Line.append(x)

    X.append(Line)

#Resultado
print(trocar_coluna(X))
