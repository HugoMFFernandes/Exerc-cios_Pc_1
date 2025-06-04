
def define_mat(x): 
    n = len(x) 
    y = [[0]*n for i in range(n)]  
    for i in range(n): 
        for j in range (n): 
            y[i][j]=(i+1)*x[j] 
    for i in range(1,n-1,2): 
        for j in range(n): 
            y[i][j]=y[i-1][j]+y[i+1][j] 
    y[i][j]=0    
    return y 


X = [1,4,2,-3] 
B = define_mat(X) 
for i in range(len(B)):
    print(B[i])