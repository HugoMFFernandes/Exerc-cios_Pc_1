#Seja A uma matriz (m x n). Escrever um algoritmo para transformar a matriz A trocando a primeira linha com a última. 

from modulo_acesso_ficheiros import*

#Defenir a função
def trocar_linha(A):
    aux=A[0]
    A[0]=A[len(A)-1]
    A[len(A)-1]=aux
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
print(trocar_linha(X))