import numpy as np
import scipy.linalg as linalg
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5

print("\n=== ЗАДАНИЕ 1 (стр. 87) ===")
# Полином через 4 точки

x_int1 = np.array([-1, 1, 3, mu+4])
y_int1 = np.array([8, 6+theta, 6, nu])

# Находим коэффициенты полинома 3-й степени
A_poly = np.column_stack([np.ones(len(x_int1)), x_int1, x_int1**2, x_int1**3])
c_poly = np.linalg.solve(A_poly, y_int1)

print(f"Уравнение полинома: y = {c_poly[0]:.4f} + {c_poly[1]:.4f}*x + {c_poly[2]:.4f}*x^2 + {c_poly[3]:.4f}*x^3")

x_star = [-2, 0.5]
for xs in x_star:
    y_val = c_poly[0] + c_poly[1]*xs + c_poly[2]*xs**2 + c_poly[3]*xs**3
    print(f"y({xs}) = {y_val:.4f}")