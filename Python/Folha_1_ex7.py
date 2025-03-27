#Escreva um algoritmo e um programa que determine os divisores de um número inteiro N.

N=int(input("N="))

div=[]

for i in range (1,N+1):

    if N%i==0:

        div.append(i)

print(div)