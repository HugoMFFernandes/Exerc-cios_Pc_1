import vetores as v
import math

N=int(input("Numero de componentes de X - "))

X=[0]*N
for i in range(len(X)):
    X[i]=float(input("X["+str(i+1)+"] - "))

resultado=v.vetor_norma(X)

print("A norma do vetor é",resultado)