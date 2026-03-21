import numpy as np
from scipy import linalg

alpha = 7
beta = 3
gamma = 1 
theta = 2
mu = 0
nu = 5

A = np.array([
    [3, 1, 1, gamma],
    [1, -mu, nu, 4],
    [-5, 0, -1, -7],
    [1, -6, alpha, 6]
])


b = np.array([alpha, beta, -5, 3]).reshape(4,1)

x = linalg.solve(A,b)

for i in range(len(b)):
    print(f"x({i+1}) = {x[i][0]}")
