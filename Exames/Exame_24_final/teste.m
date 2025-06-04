a=0;
b=1;
N=11;
k=2:N+1;
h=0.1;
X=a:h:b;
Y=pi./(2*k);

[A,B]=define_matrizes(X,Y,@avalia_fx);
disp('-------Matriz A-------')
disp(A);
disp('-------Matriz B-------')
disp(B);