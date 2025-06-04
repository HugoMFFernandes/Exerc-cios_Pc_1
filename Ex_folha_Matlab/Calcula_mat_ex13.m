function [A,B] = calcula_mat_ex13(X,f,g)
    N=length(X);
%Matriz A
    A=ones(2,3);
    A(1,1)=sum(f(X.^2));
    A(1,2)=sum(X.*f(X));
    
    ind=[2:N-1];
    A(1,3)=sum(f(X(ind))-g(X(ind+1)));

    A(2,1)=sum(f(X).^2);
    A(2,2)=sum(g(X));
   
    ind=[1:2:N];
    A(2,3)=sum((f(X(ind)).^2));

%matriz B
    X=X';
    B=X;
    for i = 2:N
        B=[B X.^i];
    end

end