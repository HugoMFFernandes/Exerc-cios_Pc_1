a = input('Limite inferior do intervalo - ');
b = input('Limite superior do intervalo - ');
N = input('Numero de pontos que vamos avaliar - ');

x_i=linspace(a,b,N)
valores_fx=def_f(x_i)




disp(valores_fx)