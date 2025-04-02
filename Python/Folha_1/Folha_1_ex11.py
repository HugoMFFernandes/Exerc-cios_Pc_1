#Considere a função random.randint(a,b) que gera números inteiros aleatórios entre a e b. 
#Escreva um programa que gera números aleatórios inteiros entre 1 e 50 e determina o primeiro 
#que seja múltiplo de 3.


import random

t=random.randint(1,50)

while t%3!=0:
    print(t)
    t=random.randint(1,50)

print(t)

