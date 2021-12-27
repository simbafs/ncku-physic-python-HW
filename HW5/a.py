import numpy as np
import matplotlib.pyplot as plt

# debug mode
debug = True

J = []
B = []

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

    j = lambda t: xm*np.power(np.e, -b*t)*(
            -1*np.power(b, 3)*np.power(w, 0)*np.cos(w*t)
            -3*np.power(b, 2)*np.power(w, 1)*np.sin(w*t)
            +3*np.power(b, 1)*np.power(w, 2)*np.cos(w*t)
            +1*np.power(b, 0)*np.power(w, 3)*np.sin(w*t)
        )

    mj = 0

    while t < 10:
        x = j(t)
        if(abs(x) > abs(mj)):
            mj = x
        t = t + dt
    return mj

t = 0
beta = lambda t: 2*np.pi/T101*t
while t < 1:
    x = 2*m*beta(t)
    y = f(beta(t))
    if(debug):
        B.append(x)
        J.append(y)

    if(y < 0.05):
        print("damping coefficient need", x)
        break

    t = t + dt

if(debug):
    plt.grid()
    plt.plot(B, J, label="J", color='blue')
    plt.title('b-maxj')
    plt.xlabel('b')
    plt.ylabel('max j')
    plt.legend()
    plt.show()
