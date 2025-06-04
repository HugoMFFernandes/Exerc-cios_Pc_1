from random import*
from modulo_acesso_ficheiros import*
num_lines=int(input("Numero de linhas - "))
num_columns=int(input("Numero de colunas - "))
X=[[0]*num_columns for i in range(num_lines)]
for i in range(num_lines):
    for j in range(num_columns):
        X[i][j]=randint(-10,10)

escreve_matriz_ficheiro("matriz_X.txt",X)
print(X)