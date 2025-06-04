def define_mat(n): 
 
    x=[[0]*n for i in range(n)] 
    for j in range(n): 
        x[0][j]=1 
    for i in range(1,n): 
        x[i][0]=2 
        for j in range(1,n): 
            x[i][j]=x[i][j-1]+x[i-1][j] 
    return x 

n=int(input("introduza um número > 1: ")) 
B= define_mat(n) 

print(B)