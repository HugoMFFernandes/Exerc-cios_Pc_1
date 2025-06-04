function [A,B,C] = altera_mat(A,B,C)
    % Elimina a ultima linha da matriz C
    C(end-1,:)=[];

    % Acrescenta à Matriz A as colunas de B de índice ímpar
    A=[A B(:,1:2:end)];

    % Elimina linhas de B de índice par
    B(2:2:size(B,1),:)=[];
    
end