from random import*

letras=["e","g","g","i","n","r"]
palavra=""
cont=0
while palavra!=letras[4]+letras[3]+letras[2]+letras[1]+letras[0]+letras[5]:
    palavra=""
    for i in range(len(letras)):
        num=randint(0,5)
        palavra=str(palavra)+str(letras[num])
    print(palavra)
    cont+=1
print("Esta merda demorou",cont,"ciclos")
