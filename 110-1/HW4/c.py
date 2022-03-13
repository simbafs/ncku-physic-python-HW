import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def f(L):
    T = []
    Theta = []
    X = []
    
    # const
    dt = 0.001
    g = -9.8
    
    # params
    #  L = 0.3
    
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
        Theta.append(-L*math.cos(theta))
        X.append(x)
    
        # calc
        t += dt
        if(theta >= wTheta):
            flag = False
            tr = t
            alpha = 3*g*math.sin(math.pi/2-theta)/(2*L)
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
            return tr/tb
            break

a = f(0.3)
b = f(0.4)
print("======================")
print("the rod of the length L", "doesn't" if a == b else "does" , "affect the ratio")
print("======================")


#  plt.grid()
#  plt.title('x-y')
#  plt.xlabel('t')
#  plt.ylabel('x')
#  plt.plot(T, Theta, label="rod", color='blue')
#  plt.plot(T, X, label="ball", color='red')
#  plt.show()
