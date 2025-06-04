function [fx] = define_fx(x)
    fx=(1+x).*sqrt(sin(x.^2));
end