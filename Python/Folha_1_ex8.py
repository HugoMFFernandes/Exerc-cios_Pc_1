# Escreva um algoritmo e um programa para verificar se um número natural N é um número perfeito. Número perfeito é aquele que é igual à soma de todos os seus divisores, excluindo ele próprio.

N=int(input("N="))

Soma=0

for i in range(1,N):
    if N%i==0:
        Soma=Soma+i


if Soma==N:
    print(N,"é um número perfeito")

else:
    print(N,"não é um número perfeito")
