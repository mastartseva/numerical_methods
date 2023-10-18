import sympy as sm

def func(x):
    return (x - 2) * ((x - 1) ** 3) * ((x - 3) ** 2)

x=sm.Symbol('x')
f=sm.diff((x - 2) * ((x - 1) ** 3) * ((x - 3) ** 2),x)

     
def newton1(x0,e,c):
    x=sm.Symbol('x')
    x1=x0-c*func(x0)/f.subs(x,x0)
    x2=x1
    while abs((x2-x1)/(1-x2-x1/(x1-x0)))>=e:
        x2=x1-c*func(x1)/f.subs(x,x1)
        if abs(func(x2))<abs(func(x1)):
            c+=1
        x0=x1
        x1=x2
    return x1

print(newton1(5,0.01,2))