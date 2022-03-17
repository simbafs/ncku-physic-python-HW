# Import libraries
import math
import numpy as np
import matplotlib.pyplot as plt

bar = False

print("do you want to see the progress bar? need to install `tqdm`(y/N) ", end="")
if input().lower() == "y":
    import tqdm as tqdm
    bar = True

# Constants
eps = 8.854187817e-12
sigma0 = 1
R = 5
w = 7
littleNum = 1e-4

# params
nTheta = 60
nR = 10
interval = 31
#  interval = 201j
# k is the middle index of X, Y, Z 
K = int((abs(interval)-1)/2)

# testing function, delete later
def angle(x, y):
    t = math.atan2(y, x)
    return t

def csv(En):
    for i in range(interval):
        for j in range(interval):
            print(En[i][j], end=", ")
        print()
    print()

coordi = np.linspace(-w, w, interval)

# equal return if the two number is very close to each other [tested]
def equal(a, b, n=littleNum):
    return abs(a - b) < n

#  #  test of equal
#  print("equal test:")
#  print(equal(0, 0)) # passed
#  print(equal(0.1, 0.2)) # passed
#  print(equal(0.1, 0.1+1e-5)) # passed

# r return r^2 of p1 and p2 [tested]
def r2(x1, y1, z1, x2, y2, z2):
    r = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
    # to prevent E -> infinity, if r is very small, return 0
    if equal(r, 0):
        return 0
    return r

def dQ(r):
    return sigma0 * r * 2 * np.pi * R**2 / (nR * nTheta)

# dQ return the charge at the point (x, y, z)
def dq(i, r):
    theta = 2 * np.pi * i / nTheta
    return np.array([r * np.cos(theta), r * np.sin(theta), 0])

# E return the electric field at the point (x, y, z) [untested]
# BUG: Ez is always 0
def E(x, y, z):
    En = np.array([0, 0, 0])
    _r = r2(x, y, z, 0, 0, 0)**0.5
    #  print("x, y, z")
    #  print(x,y,z, sep=", ")
    #  print("r, qx, qy, qz, Ex, Ey, Ez")
    for r in range(nR):
        for i in range(nTheta):
            q = dq(i, _r)
            r = r2(x, y, z, *q)**0.5
            if equal(r, 0):
                continue
            #  print(r2(*dq(i, r), 0,0,0)**0.5, *dq(i, r), *(dQ(r) / (4 * np.pi * eps * r) * np.array([x-q[0], y-q[1], z-q[2]])), sep=", ")
            En = np.add(En, dQ(r) / (4 * np.pi * eps * r**2) * np.array([x-q[0], y-q[1], z-q[2]]))
            #  if (En[2] != 0):
            #      print("Ez is not 0")

    # if E is too small, set it as 0
    for i in range(len(En)):
        if abs(En[i]) < littleNum:
            En[i] = 0

    return [En[0], En[1], En[2]]

#  # test of E(x, y, z)
#  print("test of E(x, y, z)")
#  print(E(0, 0, 0)) # passed
#  print(E(R, 0, 0)) # passed
#  print(E(0, R, 0)) # passed
#  print(E(R+littleNum, 0, 0)) # passed
#  print(E(R-littleNum, 0, 0)) # passed
#  print(E(2*R, 0, 0))
#  print(E(0, 2*R, 0))
#  print(E(0, 0, 2*R))
#  print(coordi)
#  t = E(coordi[K+1], coordi[K], R-0.5)
#  print(t, np.arctan(t[1]/t[0])*180/np.pi)
#  print(dQ(1), dQ(R))

# MoE return the magnitude of E(U, V)
#  def MoE(U, V):
#      MoEn = [[0]*interval]*interval
#      for i in range(len(U)):
#          for j in range(len(U[0])):
#              MoEn[i, j] = math.sqrt(U[i, j]**2 + V[i, j]**2)
#      return MoEn

# extractXY extract the n-th of vector from XY plane [tested]
def extractXY(En):
    R = np.array([[0]*interval]*interval)
    for i in range(interval):
        for j in range(interval):
            R[i][j] = En[i][j][K]
    return R

def extractXZ(En):
    R = np.array([[0]*interval]*interval)
    for i in range(interval):
        for j in range(interval):
            R[i][j] = En[i][K][j]
    return R

def extractYZ(En):
    R = np.array([[0]*interval]*interval)
    for i in range(interval):
        for j in range(interval):
            R[i][j] = En[K][i][j]
    return R

# a 3-D array of electric field, each element is a vector
Ex = np.zeros((interval, interval, interval))
Ey = np.zeros((interval, interval, interval))
Ez = np.zeros((interval, interval, interval))

if bar:
    pgbar = tqdm.tqdm(total=interval**3)
for i in range(interval):
    for j in range(interval):
        for k in range(interval):
            if bar:
                pgbar.update(1)
            # skip points that not display on the screen
            if (i != K) and (j != K) and (k != K):
                continue
            En = E(coordi[i], coordi[j], coordi[k])
            Ex[i][j][k] = En[0]
            Ey[i][j][k] = En[1]
            Ez[i][j][k] = En[2]

# plot

fig, (xy, xz, yz) = plt.subplots(1, 3)

fig.suptitle("Maximum the window, the title of axis will appear")

xy.set_aspect('equal')
xz.set_aspect('equal')
yz.set_aspect('equal')

xy.set_title('XY')
xz.set_title('XZ')
yz.set_title('YZ')

xy.set_xlabel('x')
xy.set_ylabel('y')

xz.set_xlabel('x')
xz.set_ylabel('z')

yz.set_xlabel('y')
yz.set_ylabel('z')

#  csv(extractYZ(Ey))
#  csv(extractYZ(Ez))

xy.streamplot(coordi, coordi, extractXY(Ey), extractXY(Ex), color='k', linewidth=1, density=1, arrowstyle='->', arrowsize=1)
xz.streamplot(coordi, coordi, extractXZ(Ez), extractXZ(Ex), color='k', linewidth=1, density=1, arrowstyle='->', arrowsize=1)
yz.streamplot(coordi, coordi, extractYZ(Ez), extractYZ(Ey), color='k', linewidth=1, density=1, arrowstyle='->', arrowsize=1)

xy.add_patch(plt.Circle((0, 0), R, color='r'))
xz.plot([0, 0], [-R, R], color='r')
yz.plot([0, 0], [-R, R], color='r')

plt.show()
