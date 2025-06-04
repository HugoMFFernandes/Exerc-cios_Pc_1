from random import*

def criar_vetor(k):
    A=[]
    cont=0
    div=[]
    while cont<3:
        num=randint(1,100)
        A.append(num)
        if num%k==0:
            cont+=1
            div.append(num)
    
    return (A,div)

k=7
A=criar_vetor(k)

print(A)