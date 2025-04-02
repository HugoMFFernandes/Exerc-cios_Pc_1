# Um aluno da FEUP já terminou N disciplinas com classificações entre 10 e 20. Escreva um algoritmo que de acordo com o valor da média das classificações, MED, permita atribuir uma nota qualitativa

N=int(input("Numeros de disciplinas -"))

Notas=[]

Soma=0

for i in range(1,N+1):
    t=int(input("Nota da disciplina -"))
    Notas.append(t)

for t in Notas:
    Soma=Soma+t

Media=Soma/N

if Media<13.5:
    print("Media Suficiente")

elif Media>=17.5:
    print("Media Muito Bom")

else:
    print("Media Bom")

