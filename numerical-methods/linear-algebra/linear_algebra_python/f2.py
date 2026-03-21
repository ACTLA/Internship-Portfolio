import numpy as np
from scipy import linalg

alpha = 7
beta = 3
gamma = 1 
theta = 2
mu = 0
nu = 5

G = np.array([
    [2, 3+alpha, 4+mu, 6],
    [beta+1, gamma, nu, 12],
    [5, -2, 16, mu+1],
    [2, 7, 11, -6]
])

det_G = linalg.det(G)
eigenvalues, _ = linalg.eig(G)
inv_G = linalg.inv(G)

print(f"Определитель матрицы G = \n{det_G}")
print(f"Собственные значения G = \n{eigenvalues.real}")
print(f"Обратная матрица = \n{inv_G}")