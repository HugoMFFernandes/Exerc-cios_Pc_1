disp('------Exercicio 13------')

%Determinar os valores a utilizar na operação
a=input('Limite inferior - ');
b=input('Limite superior - ');
N=input('N - ');

%Determinar o vetor de entrada
[X]=define_points(N,a,b);

%Calcular as matrizes
[A,B]=Calcula_mat_ex13(X,@avalia_f,@avalia_g);

disp(A)
disp(B)


