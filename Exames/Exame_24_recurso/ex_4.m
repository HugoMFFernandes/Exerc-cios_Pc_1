N=input('N - ');

seq_fib=[1,2];
for i = 3:N
    seq_fib=[seq_fib sum(seq_fib(end-1:end))];
end

mult_5=find(rem(seq_fib,5)==0 & rem(seq_fib,7)~=0);

mult_2=find(rem(seq_fib,2)==0);
maior_multiplo_2=max(mult_2);

not_prime=find(~isprime(seq_fib));
median=mean(not_prime);


disp(seq_fib)
disp(mult_5)
disp(maior_multiplo_2)
disp(median)