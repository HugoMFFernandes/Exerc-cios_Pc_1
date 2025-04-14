# Seja A uma matriz (m linhas e n colunas) e k um escalar.  
#a) Escreva um algoritmo para multiplicar uma matriz por um escalar. 
#b) Defina a função m_matriz_escalar(A,k) para calcular o produto da matriz A pelo escalar k. 

from modulo_acesso_ficheiros import *
from modulo_matrizes import*


k=float(input("Escalar - "))
A = le_matriz_de_ficheiro_de_texto("matriz_A.txt")

B=m_matriz_escalar(A,k)
print(B)
escreve_matriz_ficheiro("matriz6.txt",B)

