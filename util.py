from dataclasses import dataclass
import math

@dataclass
class VectorR: # 直角座標
    x: float
    y: float
    z: float

@dataclass
class VectorP: # 極座標
    r: float
    theta: float
    phi: float

def RtoP(V: VectorR) -> VectorP: # 直角座標轉極座標
    p = VectorP(0, 0, 0)
    p.r = math.sqrt(V.x**2+V.y**2+V.z**2)
    if(p.r == 0):
        p.theta = 0.0
    else:
        p.theta = math.acos(V.z/p.r)
    if(V.x == 0 or p.theta == 0):
        p.phi = 0.0
    else:
        p.phi = math.atan(V.y/V.x)
    return p

def PtoR(V: VectorP) -> VectorR: # 極座標轉直角座標
    p = VectorR(0, 0, 0)
    p.x = V.r*math.sin(V.theta)*math.cos(V.phi)
    p.y = V.r*math.sin(V.theta)*math.sin(V.phi)
    p.z = V.r*math.cos(V.theta)
    return p


def cross(A: VectorP, B: VectorP): # -> VectorP:
    a = PtoR(A)
    b = PtoR(B)
    c = np.cross([a.x, a.y, a.z], [b.x, b.y, b.z])
    C = RtoP(VectorR(c[0], c[1], c[2]))
    print(C)
