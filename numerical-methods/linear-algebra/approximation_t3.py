import numpy as np
import scipy.linalg as linalg
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5


print("\n=== ЗАДАНИЕ 3 (стр. 51) ===")
# Три типа аппроксимации

x = np.array([nu+mu, nu+mu+1, nu+mu+2, nu+mu+3, nu+mu+4])
y = np.array([gamma+beta, gamma+beta+1, gamma+beta+3, gamma+beta+4, gamma+beta+8])

# Парабола
def parabola(x, c0, c1, c2):
    return c0 + c1*x + c2*x**2

popt_par, _ = curve_fit(parabola, x, y)
K_par = np.sum((y - parabola(x, *popt_par))**2)
print(f"Парабола: K={K_par:.6f}")

# Экспонента
def exponential(x, a, b):
    return a * np.exp(b*x)

popt_exp3, _ = curve_fit(exponential, x, y, p0=[1, 0.1])
K_exp = np.sum((y - exponential(x, *popt_exp3))**2)
print(f"Экспонента: K={K_exp:.6f}")

# Логарифм
def logarithmic(x, a, b):
    return a + b*np.log(x)

popt_log, _ = curve_fit(logarithmic, x, y)
K_log = np.sum((y - logarithmic(x, *popt_log))**2)
print(f"Логарифм: K={K_log:.6f}")

x3_plot = np.linspace(x.min(), x.max(), 100)

plt.figure(figsize=(12, 8))
plt.plot(x, y, 'o', label='Исходные данные', markersize=10)
plt.plot(x3_plot, parabola(x3_plot, *popt_par), '-', label=f'Парабола (K={K_par:.3f})', linewidth=2)
plt.plot(x3_plot, exponential(x3_plot, *popt_exp3), '--', label=f'Экспонента (K={K_exp:.3f})', linewidth=2)
plt.plot(x3_plot, logarithmic(x3_plot, *popt_log), '-.', label=f'Логарифм (K={K_log:.3f})', linewidth=2)
plt.legend()
plt.grid(True)
plt.title('Задание 3: Сравнение методов аппроксимации')
plt.show()