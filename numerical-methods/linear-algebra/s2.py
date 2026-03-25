import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

alpha = 1
gamma = 1
upsilon = 1
mu = 1
nu = 1



# Определяем функцию
def f(x):
    return alpha*x**3 - (gamma + upsilon)*x**2 - mu*x + nu

# Находим корни
x0_guess = [0, 1, 2]  # начальные приближения
roots = []
for x0 in x0_guess:
    root = fsolve(f, x0)[0]
    roots.append(root)

print("Найденные корни:", np.unique(roots))

# График
x_vals = np.linspace(-2, 5, 100)
plt.plot(x_vals, f(x_vals))
plt.axhline(0, color='r', linestyle='--')
plt.axvline(0, color='red', linestyle='--')
plt.grid()
plt.show()
