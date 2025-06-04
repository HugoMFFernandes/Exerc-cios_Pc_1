A = [1,2,3,4,5;6,7,8,9,10; 11, 12, 13, 14, 15]; 
A(:,3)=[]; 
A(:,end)=2* A(:,end-1); 
B=A; 
A(1,:)=33; 
A(:,end)=77 ;
 
C=A; 
A(end,end)=size(A,1)*size(A,2);

disp(A)
disp(B)
disp(C)