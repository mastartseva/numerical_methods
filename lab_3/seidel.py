import numpy as np
def seidel(A,B,e,iter):
    for i in range(len(A)):
        for j in range(1,len(A)):
            if A[i,i]>abs(A[i,j])+abs(A[i,j-1]):
                x1=np.array(A[i,j])







A=np.array([[2,3,1],[4,7,2],[5,8,9]])
n=len(A)
B=np.array([2,6,8])
X=np.linalg.solve(A,B)
print(n)
