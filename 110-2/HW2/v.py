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

d = np.zeros((leng, leng, leng))

if '-l' in sys.argv:
    # load data
    loadD = np.loadtxt('data.csv') 
    loadedOriginal = loadD.reshape(loadD.shape[0], loadD.shape[1] // d.shape[2], d.shape[2])
    d = loadedOriginal
else:
    # calculate

    # CutEdge reture the closet index that n+1 and n-1 are both in range
    def CutEdge(n:int):
        if n-1 < 0:
            n = n+1
        elif n+1 >= leng:
            n = n-1
        return n

    # IsInCone test if (i,j,k) is in cone
    def IsInCone(i:int,j:int,k:int):
        return (x[i][j][k]**2 + y[i][j][k]**2)**0.5 < z[i][j][k] * np.tan(alpha)

    if bar:
        pgbar = tqdm.tqdm(total=leng**3+leng**4)

    # cone
    for i in range(leng):
        for j in range(leng):
            for k in range(leng):
                bar and pgbar.update(1)
                if IsInCone(i, j, k):
                    d[i][j][k] = 10

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
                    d[i,j,k] = (d[i+1,j,k]+d[i-1,j,k]+d[i,j+1,k]+d[i,j-1,k]+d[i,j,k+1]+d[i,j,k-1])/6

    # write to file
    np.savetxt('data.csv', d.reshape(d.shape[0], -1))

x, y = np.meshgrid(range(-n, n+1), range(-n, n+1))

fig = plt.figure("V diagram")
xz = fig.add_subplot(121)
xz.set_aspect('equal')
xz.set_title('XZ')
xz.set_xlabel('x')
xz.set_ylabel('z')

fig.colorbar(xz.contourf(x, y, np.transpose(d[n]), 30))

xy = fig.add_subplot(122)
xy.set_aspect('equal')
xy.set_title('XY')
xy.set_xlabel('x')
xy.set_ylabel('y')

fig.colorbar(xy.contourf(x, y, np.transpose(d[:,:,n]), 30))

plt.show()
