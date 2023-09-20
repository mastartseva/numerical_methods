def function(x):
    return (x - 2) * ((x - 1) ** 3) * ((x - 3) ** 2)
def halfdiv(a,b,max_iter):
    e=0.01
    iter_count=0
    if function(a)*function(b)<0 and iter_count<max_iter:
        while abs(b-a)>e:
            x0=(a+b)/2
            if function(x0)==0:
                return x0
            elif function(a)*function(x0)<0:
                b=x0
            else:
                a=x0
            iter_count+=1
        return x0       
    else:
        print("Нет корней")

a,b=map(float,input().split())    
print(halfdiv(a,b,20))


        

