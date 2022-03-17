import numpy as np

interval = 3
K = int((interval-1)/2)

def extractXY(En):
    R = np.array([[0]*interval]*interval)
    for i in range(interval):
        for j in range(interval):
            R[i][j] = En[i][j][K]
    return R

En = np.zeros((interval, interval, interval))
t = 0
for i in range(interval):
    for j in range(interval):
        for k in range(interval):
            En[i][j][k] = t
            t += 1

print(En)
print()
print(extractXY(En))
