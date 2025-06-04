function [A,B] = define_matrizes(X,f)
    N=length(X);

    %Matriz A
    A=[];

    A(end+1)=sum(X.*f(X));

    x_alt=X(2:N)-X(1:N-1);
    A(end+1)=sum(f(x_alt));

    A(end+1)=prod(f(f(X)));


    %Matriz B
    exp=(1:N);
    x_alt=X.^exp;
    B=ones(N);
    for i = 1:N
        B(i,i:N)=x_alt(i:N);
    end
    

end