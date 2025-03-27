#Ex6  Escreva um algoritmo e um programa que calcule o fatorial de um número natural.

N=int(input("N ="))

P=1

if N>0:
    for i in range(1,N+1):
        P=P*i
    print("O fatorial de",N,"e",P)

elif N==0:
    print("O fatorial de 0 e 1")

else:
    print("Nao e possivel determinar o factorial de",N)
