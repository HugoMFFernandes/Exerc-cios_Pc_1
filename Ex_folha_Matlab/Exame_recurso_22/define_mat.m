function [A] = define_mat(X,f)
    
    N=lenght(X)
    A(1,1)=f(X(1));

    ind=2:N-1;

end