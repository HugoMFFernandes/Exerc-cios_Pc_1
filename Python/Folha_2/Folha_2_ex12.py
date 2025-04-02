#Defenir a função
def recolhe_elementos_mk(X,k):
    
    Y=[]
    t=0

    for i in range(len(X)):
        if X[i]%k==0:
            Y.append(X[i])
            t=1

    if t==0:
        return False
    
    else:
        return Y

#Programa para testar a função
N=int(input("Numero de componenetes do vetor - "))
X=[0]*N
for i in range(N):
    X[i]=int(input("X["+str(i)+"] - "))

k=int(input("Escalar - "))

if recolhe_elementos_mk(X,k)==False:
    print("O vetor não tem nenhum elemento multiplo do escalar dado")

else:
    print(recolhe_elementos_mk(X,k))