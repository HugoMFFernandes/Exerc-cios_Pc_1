A=[7 0 99;8 2 1;1 5 -8]

%Defenir B a partir de A
B=[A ones(3,1)]
B(end+1,:)=3

%Defenir C a partir de B
C=B
aux=C(:,1)
C(:,1)=C(:,3)
C(:,3)=aux

%Defenir D a partir de C
aux=C'
D=[C(1:3,1:3) prod(aux(1:3,1:3))']
D=[D;sum(D(1:3,:))]
D(end,end)=D(1,1)

%Defenir E a partir de D
E=D
E(:,1:2:3)=[]
E(end,1)=E(end,1)-E(2,1)
