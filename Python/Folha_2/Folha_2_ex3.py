#Sejam A, B e C vetores e k um escalar real. Escreva um programa para calcular || (AB) C + k A || usando as funções definidas anteriormente, incluídas no módulo
import vetores as v

Na=int(input("Numero de componnenetes do vetor A - "))
A=[0]*Na
for i in range(Na):
    x=float(input("A["+str(i)+"] - "))

Nb=int(input("Numero de componnenetes do vetor B - "))
B=[0]*Nb
for i in range(Nb):
    x=float(input("B["+str(i)+"] - "))

Nc=int(input("Numero de componnenetes do vetor C - "))
C=[0]*Nc
for i in range(Nc):
    x=input("C["+str(i)+"] - ")

k=float(input("Escalar - "))

#Operações
if Na==Nb:
    if Nc==Na:
        kA=v.escalar_vetor(A,k)
        AB=v.multi_vetor(A,B)
        ABC=v.multi_vetor(AB,C)

        D=v.soma_vetores(ABC,kA)

        print(v.vetor_modulo(B))

    else:
        print("Não é possível realizar a operação")

else:
    print("Não é possível realizar a operação")