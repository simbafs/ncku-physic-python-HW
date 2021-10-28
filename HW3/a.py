import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
import math

@dataclass
class VectorR: # 直角座標
    x: float
    y: float
    z: float
    def __add__(self, b):
        return VectorR(self.x+b.x, self.y+b.y, self.z+b.z)
    def __sub__(self, b):
        return VectorR(self.x-b.x, self.y-b.y, self.z-b.z)
    #  def __mut__(self, b):
    #      if(type(b) == int or type(b) == float):
    #          return VectorR(self.x*b, self.y*b, self.z*b)

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


def cross(A: VectorR, B: VectorR) -> VectorR:
    c = np.cross([A.x, A.y, A.z], [B.x, B.y, B.z])
    C = VectorR(c[0], c[1], c[2])
    return C

def mut(A: VectorR, mut: float) -> VectorR:
    return VectorR(A.x*mut, A.y*mut, A.z*mut)

T = []
X = []
Y = []

# const
dt = 0.001
g = 9.8

# params
omega = PtoR(VectorP(7.292e-5, 66/math.pi, 0))
L = 10

# var
t = 0
r = VectorR(0, 0, 0)
v = VectorR(10, 0, 0)
#  r = PtoR(VectorP(10*math.tan(5/math.pi), 5/math.pi, 0))
#  v = VectorR(0, 0, 0)
a = VectorR(0, 0, 0)

while t < 600:
    # append
    T.append(t)
    X.append(r.x)
    Y.append(r.y)

    # calc
    t += dt
    a = mut(r, -g/L)-mut(cross(omega, v), 2)

    v.x += a.x*dt
    v.y += a.y*dt
    r.y += v.y*dt
    r.x += v.x*dt

plt.grid()
plt.title('Foucault pendulum')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(X, Y)
plt.show()

plt.grid()
plt.title('Foucault pendulum')
plt.xlabel('t')
plt.ylabel('x')
plt.plot(T, X)
plt.show()

plt.grid()
plt.title('Foucault pendulum')
plt.xlabel('t')
plt.ylabel('y')
plt.plot(T, Y)
plt.show()
