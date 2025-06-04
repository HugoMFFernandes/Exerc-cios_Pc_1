X=(1:0.2:2)

[A,B,C]=define_mat(X,@define_fx,@define_gx);

disp('-----------Matriz A-----------');
disp(A);
disp('-----------Matriz B-----------');
disp(B);
disp('-----------Matriz C-----------');
disp(C);