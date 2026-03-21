import numpy as np
import scipy.linalg as linalg
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5


print("\n=== ЗАДАНИЕ 2 (стр. 87) ===")
# Интерполяция y = c1*ln(x) + c2*x*e^(-0.5x) + c3*x^2

x_int2 = np.array([2, 3, nu+5])
y_int2 = np.array([4, mu, 24])

def basis_funcs(x):
    return np.column_stack([np.log(x), x*np.exp(-0.5*x), x**2])

A_basis = basis_funcs(x_int2)
c_basis = np.linalg.solve(A_basis, y_int2)

print(f"Коэффициенты: c1={c_basis[0]:.6f}, c2={c_basis[1]:.6f}, c3={c_basis[2]:.6f}")