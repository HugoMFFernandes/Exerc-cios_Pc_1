function [Fx] = define_fx(x)
    Fx=exp(x.^2)./(x.^2+1);
end