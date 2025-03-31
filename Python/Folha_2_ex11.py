#Defenir a função
def conta_nc_mk(X,k):
    t=0
    for i in range(len(X)):
        if X[i]%k==0:
            t=t+1
    
    return t

#Programa para testar a função
N=int(input("Numero de componenetes do vetor - "))
X=[0]*N
for i in range(N):
    X[i]=int(input("X["+str(i)+"] - "))

k=int(input("Escalar - "))

if conta_nc_mk(X,k)==0:
    print("O vetor não tem nenhum elemento multiplo",k)

else:
    print("O vetor tem",conta_nc_mk(X,k),"elementos multiplos de",k)