import numpy as np

def power_method(A,X0,e,max_iter):
    k=0
    c0=0
    while k<max_iter:
        X1=np.dot(A,X0)
        c1=X1[0]/X0[0]
        if c1-c0<=e:
            return X1
    k+=1
    X0=X1
    c0=c1
    

A=[[5,1,2],
   [1,4,1],
   [2,1,3]]

X0=[[1],
    [1],
    [1]]

print(power_method(A,X0,0.01,2))

