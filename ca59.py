# Concept Application 55 (p. 389)

from loading import ConLoad, LinLoad
import matplotlib.pyplot as plt
import numpy as np

wo = 1
L = 1

X = np.linspace(0, L, 1000)
w = []
V = []
M = []
for x in X:
    A\
    = LinLoad(2 * wo / L, x, 0)\
    + LinLoad(-4 * wo / L, x, 0.5 * L)\
    + ConLoad(-0.25 * wo * L, x, 0)
    w.append(A.w)
    V.append(A.V)
    M.append(A.M)
    
    
plt.plot(X, M)
plt.show()






