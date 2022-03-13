import math

# const
dt = 0.001
g = -9.8

# params
L = 0.3

# var
t = 0
wTheta = -math.pi/2
alpha = 0
omega = 0
theta = 0

while t <= 60:
    # append

    # calc
    t += dt
    alpha = 3*g*math.sin(theta+math.pi/2)/(2*L)
    omega = omega + alpha*dt
    theta = theta + omega*dt
    #  print("alpha =", alpha, "omega = ", omega, "theta = ", theta)
    
    if(theta <= wTheta):
        print("It take", t, "seconds to rotate 90 degree")
        break

