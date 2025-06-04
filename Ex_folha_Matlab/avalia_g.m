function [gx] = avalia_g(x)
    gx=x.*sin((pi*(1+x.^2))/2);
end