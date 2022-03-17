# Import libraries
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

import tqdm as tqdm

# Constants
eps = 8.854187817e-12
lam = 4
R = 1
w = 3
littleNum = 1e-4

# params
delta = 60
interval = 7
#  interval = 201j
dQ = lam * 2 * np.pi / delta
# k is the middle index of X, Y, Z 
K = int((abs(interval)-1)/2)

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

# dQ return the charge at the point (x, y, z) [tested]
def dq(n):
    theta = 2 * np.pi * n / delta
    return np.array([R * np.cos(theta), R * np.sin(theta), 0])

# E return the electric field at the point (x, y, z) [untested]
def E(x, y, z):
    En = np.array([0, 0, 0])
    # special case, I can't solve this with a general method
    #  if equal(r2(x, y, z, 0, 0, 0), R**2):
    #      return En
    print(r2(x, y, z, 0, 0, 0)**0.5, x, y, z)
    if r2(x, y, z, 0, 0, 0) <= R**2 and equal(z, 0):
        #  print("skip", x, y, z)
        return En
    for i in range(delta):
        r = r2(x, y, z, *dq(i))
        if equal(r, 0):
            continue
        #  if equal(r, R**2):
        #      continue
        #  print(r, *dq(i), *(dQ / (4 * np.pi * eps * r) * dq(i)), sep=", ")
        En = np.add(En, dQ / (4 * np.pi * eps * r) * dq(i))

    # if E is too small, set it as 0
    for i in range(len(En)):
        if abs(En[i]) < littleNum:
            En[i] = 0

    return [En[0], En[1], En[2]]

#  # test of E(x, y, z)
print("test of E(x, y, z)")
print(E(0, 0, 0)) # passed
print(E(R, 0, 0)) # passed
print(E(0, R, 0)) # passed
print(E(R+littleNum, 0, 0)) # passed
print(E(R-littleNum, 0, 0)) # passed
print(E(2*R, 0, 0))

# MoE return the magnitude of E(U, V)
def MoE(U, V):
    MoEn = [[0]*interval]*interval
    for i in range(len(U)):
        for j in range(len(U[0])):
            MoEn[i, j] = math.sqrt(U[i, j]**2 + V[i, j]**2)
    return MoEn

# extractXY extract the n-th of vector from XY plane
def extractXY(En, n):
    R = np.array([[0]*interval]*interval)
    for i in range(interval):
        for j in range(interval):
            R[i][j] = En[i][j][K][n]
    return R

def extractXZ(En, n):
    R = np.array([[0]*interval]*interval)
    for i in range(interval):
        for j in range(interval):
            R[i][j] = En[i][K][j][n]
    return R

def extractYZ(En, n):
    R = np.array([[0]*interval]*interval)
    for i in range(interval):
        for j in range(interval):
            R[i][j] = En[K][i][j][n]
    return R

# a 3-D array of electric field, each element is a vector
En = np.zeros((interval, interval, interval, 3))
Co = np.zeros((interval, interval, interval, 3))

#  for i in range(interval):
#      for j in range(interval):
#          for k in range(interval):
#              Co[i][j][k] = np.array([coordi[i], coordi[j], coordi[k]])
#              # TODO: can skip some calculation here
#              En[i][j][k] = E(coordi[i], coordi[j], coordi[k])

#  # plot
#  fig, (xy, xz, yz) = plt.subplots(1, 3)
#
#  xy.set_aspect('equal')
#  xz.set_aspect('equal')
#  yz.set_aspect('equal')
#
#  xy.set_title('XY')
#  xz.set_title('XZ')
#  yz.set_title('YZ')
#
#  xy.streamplot(coordi, coordi, extractXY(En, 0), extractXY(En, 1), color='k', linewidth=1, density=1, arrowstyle='->', arrowsize=1)
#  xz.streamplot(coordi, coordi, extractXZ(En, 0), extractXZ(En, 2), color='k', linewidth=1, density=1, arrowstyle='->', arrowsize=1)
#  yz.streamplot(coordi, coordi, extractYZ(En, 1), extractYZ(En, 2), color='k', linewidth=1, density=1, arrowstyle='->', arrowsize=1)
#  #  xy.streamplot(X[K], Y[K], U[K], V[K], color=MoE(U[K], V[K]), linewidth=1)
#  #  xz.streamplot(X[K], Z[K], U[K], W[:, K+1, :], color=MoE(U[K], W[K+1]), linewidth=1)
#  #  yz.streamplot(Y[K], Z[K], V[K], W[K], color=MoE(V[K], W[K]), linewidth=1)
#
#  xy.add_patch(plt.Circle((0, 0), R, color='r', fill=False))
#  xz.plot([-R, R], [0, 0], color='r')
#  yz.plot([-R, R], [0, 0], color='r')
#
#  plt.show()
