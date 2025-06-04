function [A,B,C] = define_mat(X,f,g)
    N=length(X);

    %Matriz A
    A=zeros(2);
    A(1,1)=sum(g(f(X)));
    A(1,2)=sum(f(X))*sum(g(X));
    A(2,1)=sum(f(X(2:N-1))-g(X(1:N-2)));
    for i = 1:N
        A(2,2)=A(2,2)+sum((1:2:2*1-1)./(2:2:2*i));
    end

    %Matriz B
    B=[]
    for i = 1:N
        B=[B; X.^i]
    end

    %Matriz C
    C=2*ones(N)
    C(1,1:2:end)=X(1:2:end)
    C(end,2:2:end)
end