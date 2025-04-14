# Escreva um algoritmo que define um vetor B em que i-ésimo elemento de B é igual ao elemento mínimo da linha i da matriz dada

#Imports
from modulo_acesso_ficheiros import*

#Defenir a função
def vetor_minimo_linha(A):
    X=[0]*len(A)
    for i in range(len(A)):
        min=A[i][0]
        for j in range(len(A[i])):
            if A[i][j]<min:
                min=A[i][j]
            X[i]=min

    return X


#Testar a função
print("\t ----Matriz----")
num_lines=int(input("Numero de linhas - "))
num_colums=int(input("Numero de colunas - "))
X=[]

for i in range(num_lines):
    Line=[]
    for j in range(num_colums):
        x=float(input("X["+str(i)+","+str(j)+"] - "))
        Line.append(x)

    X.append(Line)

print(vetor_minimo_linha(X))