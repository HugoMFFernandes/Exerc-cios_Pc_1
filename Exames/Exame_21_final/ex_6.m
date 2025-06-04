A=(1:10);
for i =2:10
    A=[A;A(end,:)];
end
div=(rem(A,3)==0)
[u,v]=find(rem(A,3)==0)
B=[A(div)'; u'; v']