import vetores as v

N=int(input("Numero de copmponentes do primeiro vetor - "))
X=[0]*N
for i in range(N):
    X[i]=float(input("X["+str(i)+"] - "))


Ny=int(input("Número de componenentes do segundo vetor - "))
Y=[0]*N
for i in range(N):
    Y[i]=float(input("Y["+str(i)+"] - "))

Z=v.soma_vetores(X,Y)

if Z==None:
    print("As dimensões não são compativeis")

else:
    print(Z)