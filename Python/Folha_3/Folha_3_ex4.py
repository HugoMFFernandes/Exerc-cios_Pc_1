#Escrever um algoritmo para determinar o maximo, minimo e inidces de uma matriz

#Imports
from modulo_acesso_ficheiros import*

#Função para determinar o maximo de uma matriz e os seus inidces
def max_matriz_indice(X):
    max = X[0][0]
    max_ind = []
    for i in range(len(X)):
        for j in range(len(X[i])):
            if X[i][j] > max:
                max = X[i][j]
    
    for i in range(len(X)):
        for j in range(len(X[i])):
            if max==X[i][j]:
                max_ind.append([i,j])
    
    return max,max_ind


#Função para determinar o minimo de uma matriz e os seus indices
def min_matriz_indice(X):
    min=X[0][0]
    min_ind=[]
    for i in range(len(X)):
        for j in range(len(X[i])):
            if X[i][j]<min:
                min=X[i][j]
    
    for i in range(len(X)):
        for j in range(len(X[i])):
             if min==X[i][j]:
                min_ind.append([i,j])
    
    return min,min_ind

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

print(max_matriz_indice(X))
print(min_matriz_indice(X))