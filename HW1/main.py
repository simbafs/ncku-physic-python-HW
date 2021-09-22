n = [0] * 30
n[0], n[1] = 1, 1

for i in range(20):
    if n[i] == 0:
        n[i] = n[i-1] + n[i-2]
    print(n[i])
