import math

def media_desvio(X):
    sum=0
    for i in range(len(X)):
        sum=sum+X[i]
    
    avg=sum/len(X)

    sum=0

    for i in range(len(X)):
        sum=sum+(X[i]-avg)**2
    
    st=math.sqrt(sum/len(X))

    return ("A media das temperaturas é",avg,"e o desvio padrão",st)




N=int(input("Numero de temperaturas - "))

X=[0]*N
for i in range(N):
    x=float(input("X["+str(i)+"] - "))
    X[i]=x

print(media_desvio(X))
