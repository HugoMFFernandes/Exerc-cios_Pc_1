function [A,B,C]=gera_matrizes(M,N)
    %Calcular Matriz A
    A=2*ones(N)+5*eye(N);
    %Calcular Matriz B
    B=3*ones-6*tril(ones(N))+12*eye(N);
    %Calcular Matriz C
    C=(2:N+1);
    for i = 2:M
        C_lin=(C(end,1)+1:(N+i));
        C=[C;C_lin];
    end
end
