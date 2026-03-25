import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def system(vars):
    x, y = vars
    eq1 = 3*np.log(x) + y*np.sin(x) + y**2 - 12
    eq2 = x/(y**2 + 1) + 2**x - 3*y**2 - 22
    return [eq1, eq2]
# Численное решение
sol = fsolve(system, [2, 1])
print(f"Решение: x = {sol[0]}, y = {sol[1]}")

# Графическое решение
x_vals = np.linspace(0.1, 50, 100)
y_vals = np.linspace(-50, 50, 100)
plt.axhline(0, color='red', linestyle='--')
plt.axvline(0, color='red', linestyle='--')
X, Y = np.meshgrid(x_vals, y_vals)

Z1 = 3*np.log(X) + Y*np.sin(X) + Y**2 - 12
Z2 = X/(Y**2 + 1) + 2**X - 3*Y**2 - 22

plt.contour(X, Y, Z1, levels=[0], colors='g')
plt.contour(X, Y, Z2, levels=[0], colors='b')
plt.grid()
plt.show()


