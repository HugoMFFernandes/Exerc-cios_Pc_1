#Defenir a função
def novo_elimina_repete(X):
    Y=[X[0]]
    for i in range(1,len(X)):
        cont=0
        for j in range(len(Y)):
            if Y[j]==X[i]:
                cont=cont+1

        if cont==0:
            Y.append(X[i])

    return Y

#Testar função
N=int(input("N - "))
X=[0]*N
for i in range(N):
    X[i]=float(input("X["+str(i)+"] - "))

print(novo_elimina_repete(X))