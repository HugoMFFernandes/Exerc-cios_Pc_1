N=11;
a=0;
b=1;
h=(b-a)/(N-1);
k=(1:N);
X=a+(k+1)*h;
[A,B]=define_mat(X,@define_fx);

disp(X)
disp('Matriz A')
disp(A)
disp('Matriz B')
disp(B)