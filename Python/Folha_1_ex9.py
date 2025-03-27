#Dado um conjunto de números inteiros escreva um algoritmo e um programa para calcular:
# A média aritmética dos elementos do conjunto; 
# O primeiro elemento mínimo e a sua posição; 
# O último elemento máximo e a sua posição; 
# O número de ocorrências do elemento máximo 
#Exemplo: para X={2, 5, 1, 9, 10, 2, 20, 5 ,1, 20 ,15}. O primeiro elemento mínimo é igual a 1 e está na posição 3, último elemento máximo é 20 e está na posição 10 e o número de ocorrências do elemento máximo é igual a 2. 

Numero_elementos=int(input("Número de elemntos na lista -"))

Lista=[]

for i in range(1,Numero_elementos+1):
    elemento=int(input("elemento -"))
    Lista.append(elemento)

print(Lista)

#Média dos elementos da lista
Soma=0
for elemento in Lista:
    Soma=Soma+elemento

print("Média -",Soma/Numero_elementos)

#Primeiro minimo da lista
posicao_min=1
minimo=Lista[0]
for elemento in Lista:
    if minimo>elemento:
        minimo=elemento

    
for elemento in Lista:
    if elemento>minimo:
        posicao_min=posicao_min+1
    
    else:
        break

print("Mínimo -", minimo)
print("Posição do primeiro mínimo -", posicao_min)


#Último máximo da lista

maximo=Lista[0]
for elemento in Lista:
    if maximo<=elemento:
        maximo=elemento

#Número de ocorências do elemento máximo
Numero_max=0
for elemento in Lista:
    if elemento==maximo:
        Numero_max=Numero_max+1

#Posição do último máximo

posicao_max=0

a=0

for elemento in Lista:
    if elemento<maximo:
        posicao_max=posicao_max+1
    
    else:
        posicao_max=posicao_max+1

        a=a+1

        if a==Numero_max:
            break
            


print("Máxmo -", maximo)
print("Posição do último máximo -", posicao_max)
print("Número de ocorências do máximo -", Numero_max)