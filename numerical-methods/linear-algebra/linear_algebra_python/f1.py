import numpy as np
from scipy import linalg

alpha = 7
beta = 3
gamma = 1 
theta = 2
mu = 0
nu = 5

A = np.array([
    [2, 3+alpha, 4-mu],
    [beta, gamma, nu],
    [5, 10*mu, -2]
])

B = np.array([
    [beta, -3, 4+mu],
    [alpha, 4, nu],
    [5*mu, 10, -2]
])

C = np.array([
    [-1, 3+mu, 4-nu],
    [2, 1, nu],
    [5, 5-mu, -2]
])

print(f"A*B*С = \n{(A.dot(B)).dot(C)}")
