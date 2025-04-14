from modulo_acesso_ficheiros import*

def vetor_max(X):
    Y=[]
    for i in range(len(X)):
        max=X[i][0]
        for j in range(1,len(X[i])):
            if X[i][j]>max:
                max=X[i][j]
        Y.append(max)
    
    return Y

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
print(vetor_max(X))