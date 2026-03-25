import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

# Параметры (замените на свои)
alpha = 1
v = 1

# Определяем функцию
def f(x):
    return (v + x)**3 - 2*x**2 - alpha*x - 17


# Решаем уравнение
sol = root(f, x0=0)  # начальное приближение x0=0
print(f"Корень уравнения: x = {sol.x[0]:.6f}")


# График для отделения корней
x_vals = np.linspace(-5, 5, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='red', linestyle='--')
plt.axvline(0, color='red', linestyle='--')
plt.grid()
plt.legend()
plt.show()

