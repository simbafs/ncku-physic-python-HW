from math import factorial
import numpy as np
import matplotlib.pyplot as plt

def F(X):
    r = [0.0]*len(X)

    for i in range(0, len(X)):
        x = X[i]
        for n in range(0, 20):
            r[i] += np.power(-1, n) * np.power(x, 2*n+1) / factorial(2*n+1)


    return r

X = np.linspace(-10, 10, 200)
Ye = F(X)
Yt = np.sin(X)

plt.xlim(-10, 10)
plt.ylim(-2, 2)
plt.xlabel('x value=')
plt.ylabel('y value=')
plt.title('example')

#  plt.plot(x, y1, label='D')
plt.plot(X, Yt, '.', label='theory')
plt.plot(X, Ye, label='experiment')

plt.legend()
plt.grid()
plt.show()
