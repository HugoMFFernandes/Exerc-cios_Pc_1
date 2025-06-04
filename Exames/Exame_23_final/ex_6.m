a=1;
b=2;
N=11;
k=1:N;
X_num=k*(b-a);
X=X_num./(k+2);
[A,B]=define_matrizes(X,@avalia_fx);

disp('-------Matriz A-------')
disp(A)
disp('-------Matriz B-------')
disp(B)