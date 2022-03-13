import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

T = []
Xr = []
Xb = []

# const
dt = 0.001
g = -9.8

# params
L = 0.3

# var
t = 0
tr = 0
## rod
wTheta = -math.pi/2
alpha = 0
omega = 0
theta = 0

## ball
tb = 0
a = g
v = 0
x = 0
wX = -L

while t <= 60:
    flag = True
    # append
    T.append(t)
    Xr.append(L*math.sin(theta))
    Xb.append(x)

    # calc
    t += dt
    if(theta >= wTheta):
        flag = False
        tr = t
        alpha = 3*g*math.sin(theta+math.pi/2)/(2*L)
        omega = omega + alpha*dt
        theta = theta + omega*dt
        #  print("alpha = ", alpha, "omega = ", omega, "theta = ", theta)

    if(x >= wX):
        flag = False
        tb = t
        v = v + a*dt
        x = x + v*dt
    
    if(flag):
        print("L = ", L)
        print("The rod took", tr, "s, the ball took", tb, "s")
        print("The", "ball" if  tr > tb else "rod", "hit the ground first")
        print("Ratio between is", tr/tb)
        break

plt.grid()
plt.plot(T, Xr, label="rod", color='blue')
plt.plot(T, Xb, label="ball", color='red')
plt.title('x-y')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.show()
