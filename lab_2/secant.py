import math 
import matplotlib.pyplot as mt
import numpy as np

def function(x):
    return ((math.cos(x))-x+1)

def secant(e,x0,x):
    x1=x-function(x)*(x-x0)/(function(x)-function(x0))
    if abs(x1-x)<e:
        return x1
    x0=x
    x=x1

print(secant(0.00001, 4, 3))



