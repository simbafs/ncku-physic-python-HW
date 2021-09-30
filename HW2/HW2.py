import numpy as np
import matplotlib.pyplot as plt

T = []
A = []
V = []
Y = []

# const
m = 5
hpCAr = 1/2*1.3*0.5*np.pi*0.5*0.5 # 1/2pCAr
dt = 0.001
g = -9.8

# var
v = 0
a = g
y = 100
t = 0

while y > 0:
    # append
    T.append(t)
    A.append(a)
    V.append(v)
    Y.append(y)

    # calc
    a = g + hpCAr*v*v/m
    v += a*dt
    y += v*dt
    t += dt

plt.xlabel('t(s)')
plt.grid()
plt.ylabel('a(ms^-3)')
plt.title('a-t')
plt.plot(T, A)
plt.show()

plt.xlabel('t(s)')
plt.grid()
plt.ylabel('v(ms^-2)')
plt.title('v-t')
plt.plot(T, V)
plt.show()

plt.xlabel('t(s)')
plt.grid()
plt.ylabel('y(ms^-1)')
plt.title('y-t')
plt.plot(T, Y)
plt.show()
