import matplotlib.pyplot as plt

def create_polynom(par,i):
    def basic(x0):
        multiplication=1
        derivate=1
        for j in range(len(par)):
            if i!=j:
                multiplication*=(x0-par[j])
                derivate*=(par[i]-par[j])
        return multiplication/derivate
    return basic

def lagrange(par,y):
    polynom=[]
    for i in range(len(par)):
        polynom.append(create_polynom(par,i))

    def interpolation_polynom(x0):
        result=0
        for i in range(len(par)):
            result+=polynom[i](x0)*y[i]
        return result
    return interpolation_polynom

par=[2,3,4,5]
y=[7,5,8,7]
lag_pol = lagrange(par, y)


y2 =(lag_pol)

# Построение графика
plt.xlabel("x")         # ось абсцисс
plt.ylabel("y1, y2")    # ось ординат
plt.grid()              # включение отображение сетки
plt.plot(par, y2)  # построение графика
for x in par:
    print("x = {:.4f}\t y = {:4f}".format(x,lag_pol(x)))