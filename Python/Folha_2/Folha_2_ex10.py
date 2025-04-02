# Escreva um algoritmo que para dois vetores, X e Y troca os elementos de X dos índices ímpares com os elementos correspondentes de Y. 
#a) Escreva uma função troca_elementos (X, Y) que implementa o algoritmo anterior.




#função
def troca_elementos(X,Y):
    
    if Nx==Ny:
        for i in range(0,Nx-1,2):
            Y[i+1]=X[i]
    
        return (X,Y)
    
    else:
        return False

Nx=int(input("Numero de componentes de X - "))
Ny=int(input("Numero de componentes de Y - "))
X=[]
Y=[]

if troca_elementos(X,Y)==False:
    print("Os vetores têm número de componentes diferentes")

else:  
    for i in range(1,Nx+1):
        x=float(input("x - "))
        X.append(x)


    for i in range(1,Ny+1):
        y=float(input("y - "))
        Y.append(y)

        print(troca_elementos(X,Y))
