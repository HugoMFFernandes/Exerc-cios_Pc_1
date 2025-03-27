#ex_2 Raiz de equaçao do 2 grau 

import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

delta=b*b-4*a*c

if delta>0:

    x1=(-b+math.sqrt(delta))/2
    x2=(-b-math.sqrt(delta))/2

    print("x =",x1," e x =",x2)

elif delta==0:

    x1=-b/2

    print("x =", x1)

else:

    print("A equaçao nao tem solucoes reais")