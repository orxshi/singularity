# Concept Application 56 (p. 390)

from loading import ConLoad, ConMoment, UniLoad
import numpy as np


X = np.linspace(0, 3.6, 1000)
w = []
V = []
M = []
for x in X:
    A\
    = UniLoad(1.5, x, 0.6)\
    + UniLoad(-1.5, x, 1.8)\
    + ConLoad(-2.60, x, 0)\
    + ConLoad(1.2, x, 0.6)\
    + ConMoment(1.44, x, 2.6)
    w.append(A.w)
    V.append(A.V)
    M.append(A.M)


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def getV(x):
    i = find_nearest(np.array(X), value=x)
    return V[i]

def getM(x):
    i = find_nearest(np.array(X), value=x)
    return M[i]

print(getV(1.8), getM(1.8))