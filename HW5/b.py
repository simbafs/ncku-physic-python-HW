import numpy as np
import matplotlib.pyplot as plt

X = []
V = []

# const
dt = 0.1

# param
T101 = 6.8
m = 660e3
xm = 0.2

W = 2*np.pi/T101 # omega_0

# f returns max j with given arguments
def f(b):
    t = 0
    w = np.sqrt(W**2-b**2) #omega_1

    x = lambda t: xm*np.power(np.e, -b*t)*np.cos(w*t)
    v = lambda t: xm*np.power(np.e, -b*t)*(-np.cos(w*t)-np.sin(w*t))

    while t < 10:
        X.append(x(t))
        V.append(v(t))
        t = t + dt


    #  print("b =", b, "mj =", mj)

    plt.grid()
    plt.plot(X, V, label="V", color='blue')
    plt.title("x-v")
    plt.xlabel('x')
    plt.ylabel('v')
    plt.legend()
    plt.show()

    return 

f(6.472112795552417e-05)
