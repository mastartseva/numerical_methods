import sympy as sm

x=sm.Symbol('x')
f=sm.diff((x - 2) * ((x - 1) ** 3) * ((x - 3) ** 2),x)

def func(x):
    return (x - 2) * ((x - 1) ** 3) * ((x - 3) ** 2)

def simplified_newton(x0,e):
    x=sm.Symbol('x')
    x1=x0-func(x0)/f.subs(x,x0)
    x2=x1
    while abs((x2-x1)/(1-x2-x1/(x1-x0)))>=e:
        x2=x1-func(x1)/f.subs(x,x0)
        x1=x2
    return x1

print(simplified_newton(4,0.01))