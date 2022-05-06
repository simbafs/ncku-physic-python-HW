# Usage:
#   -p     show progress bar
#   -l     load saved data(skip calculation)

import numpy as np
import matplotlib.pyplot as plt
import sys

bar = False

if '-p' in sys.argv:
    import tqdm as tqdm
    bar = True

n = 30
leng = 2*n+1
delta = 1e-3
alpha = 15/180*np.pi

x = range(-n, n+1)
y = range(-n, n+1)
z = range(-n, n+1)
x, y, z = np.meshgrid(x, y, z)

v = np.zeros((leng, leng, leng))

# CutEdge reture the closet index that n+1 and n-1 are both in range
def CutEdge(n:int):
    if n-1 < 0:
        n = n+1
    elif n+1 >= leng:
        n = n-1
    return n

# IsInCone test if (i,j,k) is in cone
def IsInCone(i:int,j:int,k:int):
    return (x[i][j][k]**2 + y[i][j][k]**2)**0.5 <= z[i][j][k] * np.tan(alpha)

if '-l' in sys.argv:
    # load data
    loadD = np.loadtxt('data.csv')
    loadedOriginal = loadD.reshape(loadD.shape[0], loadD.shape[1] // v.shape[2], v.shape[2])
    v = loadedOriginal
else:
    # calculate
    if bar:
        pgbar = tqdm.tqdm(total=leng**3+leng**4)

    # cone
    for i in range(leng):
        for j in range(leng):
            for k in range(leng):
                bar and pgbar.update(1)
                if IsInCone(i, j, k):
                    v[i][j][k] = 10

    #  calculus
    for o in range(leng):
        for i in range(leng):
            for j in range(leng):
                for k in range(leng):
                    bar and pgbar.update(1)
                    i = CutEdge(i)
                    j = CutEdge(j)
                    k = CutEdge(k)
                    if IsInCone(i,j,k):
                        #  print(i,j,k)
                        continue
                    v[i,j,k] = (v[i+1,j,k]+v[i-1,j,k]+v[i,j+1,k]+v[i,j-1,k]+v[i,j,k+1]+v[i,j,k-1])/6

    # write to file
    np.savetxt('data.csv', v.reshape(v.shape[0], -1))

X, Y = np.meshgrid(range(-n, n+1), range(-n, n+1))

fig = plt.figure("V diagram")
xz = fig.add_subplot(121)
xz.set_aspect('equal')
xz.set_title('XZ')
xz.set_xlabel('x')
xz.set_ylabel('z')

xz.plot([0,n*np.tan(alpha)], [0, n], color='blue')
xz.plot([0,-n*np.tan(alpha)], [0, n], color='blue')

fig.colorbar(xz.contourf(X, Y, np.transpose(v[n]), 30))

xy = fig.add_subplot(122)
xy.set_aspect('equal')
xy.set_title('XY')
xy.set_xlabel('x')
xy.set_ylabel('y')

fig.colorbar(xy.contourf(X, Y, np.transpose(v[:,:,n]), 30))

plt.show()


# electric field

Exz = np.gradient(np.transpose(v[n]))
Exy = np.gradient(np.transpose(v[:, :, n]))

fig = plt.figure("E diagram")
xz = fig.add_subplot(121)
xz.set_aspect('equal')
xz.set_title('XZ')
xz.set_xlabel('x')
xz.set_ylabel('z')

xz.plot([0,n*np.tan(alpha)], [0, n], color='blue')
xz.plot([0,-n*np.tan(alpha)], [0, n], color='blue')

xz.streamplot(X, Y, Exz[1], Exz[0], density = 0.5)

xy = fig.add_subplot(122)
xy.set_aspect('equal')
xy.set_title('XY')
xy.set_xlabel('x')
xy.set_ylabel('y')

xy.streamplot(X, Y, Exy[1], Exy[0], density = 0.5)

plt.show()
