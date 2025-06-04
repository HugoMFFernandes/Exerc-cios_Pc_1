function [X] = altera_mat(X) 
       for i = 1:size(X,1) 
          id = find (isprime (X(i,:)) & X(i,:) < 25); 
              X(i,id)=33; 
          end 
             X 
         X=[X ; sum(X); max(X)]; 
end