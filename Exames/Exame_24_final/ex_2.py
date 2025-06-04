''' Seja K um número natural. Escreva em linguagem Python: 
a) uma função que cria um vetor A formado pelos divisores de K. 
b) um programa que usa a função anterior e transforma o vetor A da seguinte forma: cada elemento é 
substituído pelo produto dele próprio com os elementos seguintes. 
(o último elemento do vetor não é alterado.) '''

def divores_k(k):
    
    div=[1]
    N=k//2
    for i in range(2,N+1):
        if k%i==0:
            div.append(i)
        
    div.append(k)

    return div

k=int(input("k - "))

A=divores_k(k)

for i in range(len(A)-1):
    prod=1
    for j in range(i,len(A)):
        prod*=A[j]
    A[i]=prod

print(A)

