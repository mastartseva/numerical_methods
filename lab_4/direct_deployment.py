from sympy import symbols
import sympy
import numpy as np

def eigenvalues(A):
    q = symbols('q')
    for i in range(len(A)):
        for j in range(len(A)):
            if j == i:
                A[i][j]=(q-A[i][j])
            det=A[0][0]*(A[1][1]*A[2][2]-A[2][1]*A[1][2])
            -A[0][1]*(A[1][0]*A[2][2]-A[2][0]*A[1][2])
            +A[0][2]*(A[1][0]*A[2][1]-A[2][0]*A[1][1])
        q_arr=sympy.solve(det, q)
    return q_arr
def eigenvectors(A, q_arr):
    x1, x2, x3=symbols('x1 x2 x3')
    #x2=symbols('x2')
    #x3=symbols('x3')
    x=[[x1],
    [x2],
    [x3]]
    j=0
    for i in range(len(A)):
        while j<len(q_arr):
            A[i][i]=(q_arr[j]-A[i][i])
        j+=1
    multiplication=np.dot(A, x)
    return multiplication, eigenvalues(A)
    