#Escreva um algoritmo que a partir de dois vetores determina um vetor que inclui as componentes dos vetores dados sem elementos repetidos.

#Defenir a função
def vetor_sem_repetidos(X,Y):
    cont=0
    W=[]
    
    for i in range(len(X)):
        for j in range(len(Y)):
            lista_Y=[]
            if X[i]==Y[j]:
                lista_Y.append(j)
                cont=1
        
        for k in range(len(lista_Y)):
            Y.remove(Y[k])

        if cont==0:
            W.append(X[i])

    if len(Y)==0:
        return False
    
    else:
        return (W+Y)
    

#Testar a função
Nx=int(input("Componenetes de X - "))
X=[0]*Nx
for i in range(Nx):
    X[i]=float(input("X["+str(i)+"] - "))

Ny=int(input("Componenetes de Y - "))
Y=[0]*Ny
for i in range(Ny):
    Y[i]=float(input("Y["+str(i)+"] - "))

if vetor_sem_repetidos(X,Y)==False:
    print("Os vetores têm todos os mesmos elementos")

else:
    print(vetor_sem_repetidos(X,Y))

    
        
