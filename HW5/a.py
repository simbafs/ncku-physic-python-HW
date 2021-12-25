import numpy as np
import matplotlib.pyplot as plt

#  J = []
#  B = []

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

    j = lambda t: xm*np.power(np.e, -b*t)*(
            -1*np.power(b, 3)*np.power(w, 0)*np.cos(w*t)
            -3*np.power(b, 2)*np.power(w, 1)*np.sin(w*t)
            +3*np.power(b, 1)*np.power(w, 2)*np.cos(w*t)
            +1*np.power(b, 0)*np.power(w, 3)*np.sin(w*t)
        )

    mj = 0

    while t < 10:
        #  T.append(t)
        x = j(t)
        if(abs(x) > mj):
            mj = x
        #  J.append(x)

        t = t + dt


    #  print("b =", b, "mj =", mj)

    return mj

t = 0
beta = lambda t: 2*np.pi/T101*t
while t < 1:
    x = 2*m*beta(t)
    y = f(beta(t))
    #  B.append(x)
    #  J.append(y)

    if(y < 0.05):
        print("damping coefficient need", y)
        break

    t = t + dt

#  plt.grid()
#  plt.plot(B, J, label="J", color='blue')
#  plt.title('b-maxj')
#  plt.xlabel('b')
#  plt.ylabel('x')
#  plt.legend()
#  plt.show()
