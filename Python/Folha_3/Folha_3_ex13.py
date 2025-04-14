#Criar um algoritmo para verificar se é necessario verificar os aparelhos de medição
#Matriz 3*M

from modulo_acesso_ficheiros import*

#Defenir a função
def verificar_alertas(X):
    Lista=[]
    for j in range(len(X[0])):
        min=X[len(X)-5][j]
        max=X[len(X)-5][j]
        for i in range(len(X)-4,len(X)-1):
            if X[i][j]>max:
                max=X[i][j]
            if X[i][j]<min:
                min=X[i][j]
            
        if X[len(X)-1][j]>=max*2 or X[len(X)-1][j]<=min/2:
            Lista.append("Verificar")
            
        else:
            Lista.append("Não verificar")
        
    return Lista
    


#testar a função
num_days=int(input("Numero de dias analisados -"))
if num_days<5:
    print("Não há dados suficientes")

else:
    X=[[0]*3 for i in range(num_days)]
    print("\t ----Temperatura----")
    for i in range(num_days):
        X[i][0]=float(input(str(i+1)+"º dia - "))
    
    print("\t ----Salinidade----")
    for i in range(num_days):
        X[i][1]=float(input(str(i+1)+"º dia - "))
    
    print("\t ----Densidade----")
    for i in range(num_days):
        X[i][2]=float(input(str(i+1)+"º dia - "))

    Resultado=verificar_alertas(X)
    print("\t ----Verificação dos sistemas----")
    print("Termperatura da água -",Resultado[0])
    print("Salinidade da água -",Resultado[1])
    print("Densidade da água -",Resultado[2])