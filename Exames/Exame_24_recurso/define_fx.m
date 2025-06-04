function [Fx] = define_fx(X)
    Fx=(sin(X.^2+1))/(X.^2+1);
end