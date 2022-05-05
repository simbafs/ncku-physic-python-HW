# Usage:
#   -p     show progress bar

import numpy as np
import matplotlib.pyplot as plt
import sys

bar = False

if '-p' in sys.argv:
    import tqdm as tqdm
    bar = True

n = 30
leng = 2*n+1
d = np.zeros((leng, leng, leng))

# load data
loadD = np.loadtxt('data.csv') 
loadedOriginal = loadD.reshape(loadD.shape[0], loadD.shape[1] // d.shape[2], d.shape[2])
d = loadedOriginal




x, y = np.meshgrid(range(-n, n+1), range(-n, n+1))

fig = plt.figure("E diagram")
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
