import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
import math

@dataclass
class VectorR: # 直角座標
    x: float
    y: float
    z: float

@dataclass
class VectorP: # 極座標
    r: float
    theta: float
    phi: float

def RtoP(V: VectorR) -> VectorP: # 直角座標轉極座標
    p = VectorP(0, 0, 0)
    p.r = math.sqrt(V.x**2+V.y**2+V.z**2)
    if(p.r == 0):
        p.theta = 0.0
    else:
        p.theta = math.acos(V.z/p.r)
    if(V.x == 0 or p.theta == 0):
        p.phi = 0.0
    else:
        p.phi = math.atan(V.y/V.x)
    return p

def PtoR(V: VectorP) -> VectorR: # 極座標轉直角座標
    p = VectorR(0, 0, 0)
    p.x = V.r*math.sin(V.theta)*math.cos(V.phi)
    p.y = V.r*math.sin(V.theta)*math.sin(V.phi)
    p.z = V.r*math.cos(V.theta)
    return p


def cross(A: VectorP, B: VectorP): # -> VectorP:
    a = PtoR(A)
    b = PtoR(B)
    c = np.cross([a.x, a.y, a.z], [b.x, b.y, b.z])
    C = RtoP(VectorR(c[0], c[1], c[2]))
    print(C)

X = []
Y = []

# const
dt = 0.001
g = -9.8

# params
omega = VectorP(7.292e-5, 66/math.pi, 0)
theta = 5/math.pi
L = 10

# var
p = VectorP(10, math.pi/2-theta, 0)
v = VectorP(5, math.pi/2+theta, 0)

while y > 0:
    # append
    r = PtoR(p)
    X.append(r.x)
    Y.append(r.y)

    # calc
    

plt.grid()
plt.ylabel('y')
plt.xlabel('x')
plt.title('Foucault pendulum')
plt.plot(X, Y)
plt.show()
