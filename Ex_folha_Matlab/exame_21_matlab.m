disp('--------Exercicio 5--------')

X=[1:0.2:2];

[A,B,C]=calcula_mat(X,@define_fx,@avalia_g);

disp(A)
disp(B)
disp(C)

disp('--------Exercicio 6--------')

A=(1:10)
for i=2:10
    A=[A;A(end,:)]
end

[u,v]=find(mod(A,3)==0);
B=[A(mod(A,3)==0)';u';v'];

disp(B)




