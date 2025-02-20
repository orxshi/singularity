# Concept Application 55 (p. 389)

from loading import ConLoad, ConMoment, UniLoad
import matplotlib.pyplot as plt
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
    
    
plt.plot(X, M)
plt.show()






