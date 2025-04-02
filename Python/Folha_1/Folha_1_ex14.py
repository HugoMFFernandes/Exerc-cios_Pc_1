import math

n=0
u=1
soma=0
erro=1e-8
e=math.e

while abs(u)>erro:
    soma=soma+u
    u=-e*u/(n+1)
    n=n+1

print(soma)