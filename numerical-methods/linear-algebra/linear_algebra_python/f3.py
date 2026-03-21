import numpy as np
from scipy import linalg


A = np.array([
    [2, -5, 7],
    [8, 1, 9],
    [3., -4, 12]
])


C = np.array([
    [-25, -17, 78],
    [11, 89, 76],
    [-5, 24, 115]
])

B = linalg.inv(A).dot(C)

print(f"Матрица B = \n{B}")

