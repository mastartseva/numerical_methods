def root(number):  
    x0=0
    x=number
    e=0.001  
    while abs(x-x0)>=e:
        x0=x
        x=(x+number/x)/2
    return x

number=float(input())
sqrt=root(number)
print(sqrt)