import numpy as np

def matrix_coef(x,y):
    n=len(x)
    func=np.zeros([n,n])
    func[:,0]=y
    for j in range(1,n):
        for i in range(n-j):
            func[i][j] = \
           (func[i+1][j-1] - func[i][j-1]) / (x[i+j]-x[i])
    return func

def newton_polynomial(x,y, matrix_coef):
    n = len(y) - 1 
    polynom = matrix_coef[n]
    for k in range(1,n+1):
        polynom = matrix_coef[n-k] + (x-y[n-k])*polynom
    return polynom

x=[2,5,8,3]
y=[8,2,4,6]
mk=matrix_coef(x,y)
print(newton_polynomial(x,y,mk))