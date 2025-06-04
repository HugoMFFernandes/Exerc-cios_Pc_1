N=6


B=[1:N]
for i=2:N
    B=[B;B(1,:).^i]
end


