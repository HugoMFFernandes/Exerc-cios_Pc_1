N=input('N - ');
A=randi([0,100],N,N);
B=ones(N,1);

for i = 1:N

       primes=A(i, isprime(A(i,:)) & A(i,:)>10);

       if isempty(primes)
           B(i)=0;
       
       else
           B(i)=prod(primes);
       end
end

disp(A)
disp(B)