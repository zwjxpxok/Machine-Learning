from matplotlib import pyplot as plt
x=[0.0]
y=[1.0]
for i in range(0,10):
    y.append(1.1*y[i]-(0.2*x[i]/y[i]))
    x.append(x[i]+0.1)
plt.plot(x,y)
plt.show()
