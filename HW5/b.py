import numpy as np
import matplotlib.pyplot as plt

X = []
V = []

# const
dt = 0.01

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

    while t < 1000:
        X.append(x(t))
        V.append(v(t))
        t = t + dt

    plt.grid()
    plt.plot(X, V, label="V", color='blue', linewidth=0.5)
    plt.title("x-v")
    plt.xlabel('x')
    plt.ylabel('v')
    plt.legend()
    plt.show()

    return 

print('the v and x decrease as time go, it mean that the total energy is decreasing too. ')
f(6.472112795552417e-05)
