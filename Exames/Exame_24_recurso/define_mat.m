function [A,B] = define_mat(X,f)
    N=length(X);
    %Matriz A
    A=zeros(2);
    A(1,1)=f(X(1))+f(X(N-1))+f(X(N));
    A(1,2)=sum(f(X(2:N-1).^2));
    A(2,1)=sum(f(X(2:N)))*sum(f(X(2:N).^2));
    A(2,2)=prod(f(f(X)));

    %Matriz B
    Y=1:N;
    B=[];
    for i=1:N
        B=[B;(Y+(i-1)).^i];
    end
   
end