function [A,B,C] = calcula_mat(X,f,g)
%Defenir N
    N=length(X);
    disp(N)

%Matriz A
   A=ones(2);
   A(1,1)=sum(g(f(X)));
   A(1,2)=sum(f(X))*sum(g(X));
   A(2,1)=sum(f(X(2:N-1))-g(X(1:N-2)));

   Y=[];
   for i =1:N
        Y(end+1)=prod(1:2:2*i-1)/prod(2:2:2*i);
   end
   A(2,2)=sum(Y);

%Matriz B
    B=[1:N];
    for i=2:N
        B=[B;B(1,:).^i];
    end
    
%Matriz C
    C=2*ones(N);
    C(1,1:2:end)=X(1:2:end);
    C(end,2:2:end)=X(2:2:end);


end