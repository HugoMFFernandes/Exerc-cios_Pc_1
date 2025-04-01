def ordena_esq(X):
    Y=[]
    for i in range(len(X)):
        if X[i]<0:
            Y.append(X[i])
    
    for i in range(len(X)):
        if X[i]>0:
            Y.append(X[i])
    
    return Y

N=int(input("Numero de componentes de X - "))
X=[0]*N
for i in range(N):
    X[i]=float(input("X["+str(i)+"] - "))

print(ordena_esq(X))