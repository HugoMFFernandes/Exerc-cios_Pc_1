#Escreva uma função calcula_divisores(N) para calcular um vetor com os divisores do número N.

def calcula_divisores(N):
    X=[]
    X.append(1)
    n=1+N//2
    for i in range(2,n):

        if N%i==0:
            X.append(i)
    
    X.append(N)
    
    return X

num=int(input("Num - "))
resultado=calcula_divisores(num)
print(resultado)