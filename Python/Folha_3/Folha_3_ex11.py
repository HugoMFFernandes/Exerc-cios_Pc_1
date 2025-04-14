def linha_soma(X):
    
    for i in range(len(X[0])):
        sum=0
        for j in range(len(X)-1):
            sum+=X[j][i]
        
        X[len(X)-1][i]=sum

    return X

num_lines=int(input("Numero de linhas - "))
num_colums=int(input("Numero de colunas - "))
X=[]

for i in range(num_lines):
    Line=[]
    for j in range(num_colums):
        x=float(input("X["+str(i)+","+str(j)+"] - "))
        Line.append(x)

    X.append(Line)

print(linha_soma(X))
        