function [Fx] = define_fx(x)
    Fx=(1+x).*sqrt(sin(x.^2));
end