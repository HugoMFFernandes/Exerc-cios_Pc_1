function [B] = ex_10(N)
    B=[1];
    i=2
    while length(B)<N
        B=[B B(end)+i^2];
        i=i+1
    end

end