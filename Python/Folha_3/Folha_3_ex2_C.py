from modulo_acesso_ficheiros import*
from modulo_matrizes import*


num_lines=int(input("Numero de linhas - "))
num_colums=int(input("Numero de colunas - "))
X=[]

for i in range(num_lines):
    Line=[]
    for j in range(num_colums):
        x=float(input("X["+str(i)+","+str(j)+"] - "))
        Line.append(x)

    X.append(Line)

if num_colums==num_lines:
    print(m_matriz_dp(X))
    print(m_matriz_ds(X))

else:
    print("Não é possível realizar a operação")