function [A,B] = define_matrizes(X,Y,f)
    N=length(X);
    
    %Matriz A
    A=[];

    A(end+1)=sum(f(X).*f(Y));

    comb=X(2:N).*Y(2:N);
    A(end+1)=sum(f(comb));

    comb=X(1:N-1).*Y(1:N-1);
    A(end+1)=sum(f(f(comb)));

    x_avg=sum(X)/N;
    x_alt=X-x_avg;
    y_avg=sum(Y)/N;
    y_alt=Y-y_avg;
    denominator=(2:2:2*N);
    A(end+1)=sum(x_alt.*y_alt./denominator);


    %Matriz B
    B=zeros(3,2*N);

    B(1,1:2:2*N)=X(1:N);
    B(1,2:2:2*N)=Y(1:N);

    exp=(1:N);
    B(2,1:2:2*N)=X.^exp;
    B(2,2:2:2*N)=Y.^exp;

    for i = 1:N
        B(3,i)=prod(X(1:i));
    end

    for i = N+1:2*N
        B(3,i)=prod(Y(1:i-N-1));
    end



end