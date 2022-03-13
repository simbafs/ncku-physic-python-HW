import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import math

@dataclass
class VectorP: # 極座標
    r: float
    theta: float
    phi: float

@dataclass
class VectorR: # 直角座標
    x: float
    y: float
    z: float
    def __add__(self, b):
        return VectorR(self.x+b.x, self.y+b.y, self.z+b.z)
    def __sub__(self, b):
        return VectorR(self.x-b.x, self.y-b.y, self.z-b.z)
    def P(self) -> VectorP:
        return RtoP(self)
    #  def __mut__(self, b):
    #      if(type(b) == int or type(b) == float):
    #          return VectorR(self.x*b, self.y*b, self.z*b)

def RtoP(V: VectorR) -> VectorP: # 直角座標轉極座標
    p = VectorP(0, 0, 0)
    p.r = math.sqrt(V.x**2+V.y**2+V.z**2)
    if(p.r == 0):
        p.theta = 0.0
    else:
        p.theta = math.acos(V.z/p.r)
    if(p.theta == 0):
        p.phi = 0.0
    else:
        p.phi = math.acos(V.x/p.r)
        if V.y < 0:
            p.phi -= math.pi/2
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

def phi(x: float, y: float) -> float:
    return math.atan(y/x)*180/math.pi

T = []
X = []
Y = []
Turning = []

# const
dt = 0.001
g = 9.8

# params
omega = PtoR(VectorP(7.292e-5*5e3, 66/math.pi, 0))
#  omega = PtoR(VectorP(7.292e-5, 66/math.pi, 0))
L = 1
tolerance = 1e-3

# var
t = 0
#  r = VectorR(0, 0, 0)
#  v = VectorR(1, 0, 0)
theta = 1/math.pi
r = PtoR(VectorP(10*math.tan(theta), math.pi/2-theta, 0))
v = VectorR(0, 0, 0)
a = VectorR(0, 0, 0)
i = 0
turnAngle = 3
endPoint = PtoR(VectorP(10*math.tan(theta), math.pi/2-theta, turnAngle/180*math.pi))

v1, v2, v3 = 0, 0, 0
phiNow = 0

while True:
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
    i += 1

    v1, v2, v3 = v2, v3, v.P().r

    if(v1 >= v2 and v2 <= v3):
        if phiNow == 0:
            d = endPoint.P().phi - r.P().phi
            #  print(endPoint.P().phi, r.P().phi, d)
            if(abs(d) <= tolerance and t >= dt*10):
                #  print(r.P())
                #  print(r)
                break
        else:
            phiNow = 1-phiNow

print('turn a round take', t, 's to turn', turnAngle, 'degree')
print('so it take', t*360/turnAngle, 's to turn a round')

fig = plt.figure(figsize=(7, 6), dpi=100)
ax = fig.gca()
dot, = ax.plot([], [], color='red', marker='o', markersize=10, markeredgecolor='black', linestyle='')

def update(i):
    dot.set_data(X[i], Y[i])
    return dot,

def init():
    dot.set_data(X[0], Y[0])
    return dot,

N = len(X)
ax.grid()
ax.set_title('Foucault pendulum')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(X, Y, linewidth=0.1)
ax.scatter(r.x, r.y, s=10)
ani = animation.FuncAnimation(fig=fig, func=update, frames=N, init_func=init, interval=1000/N, blit=True, repeat=True)
plt.show()

#  plt.grid()
#  plt.title('Foucault pendulum')
#  plt.xlabel('t')
#  plt.ylabel('x')
#  plt.plot(T, X)
#  plt.show()
#
#  plt.grid()
#  plt.title('Foucault pendulum')
#  plt.xlabel('t')
#  plt.ylabel('y')
#  plt.plot(T, Y)
#  plt.show()
