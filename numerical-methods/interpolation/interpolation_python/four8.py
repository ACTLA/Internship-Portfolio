from scipy import interpolate
import numpy as np
import scipy.linalg as linalg
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt


# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5


print("\n=== ЗАДАНИЕ 8 (стр. 87) ===")
# Интерполяция радиальной базисной функцией

from scipy.interpolate import Rbf

x_rbf = np.array([1, 2, 4, 5, 7])
y_rbf = np.array([0, 1, 15+nu, mu, 8])

epsilon = mu + 2

def rbf_func(r):
    return np.sqrt(1 + (epsilon * r)**2)

rbf = Rbf(x_rbf, y_rbf, function=lambda r: np.sqrt(1 + (epsilon * r)**2))
x_star_rbf = 1.5
y_rbf_val = rbf(x_star_rbf)

print(f"Значение функции в точке x={x_star_rbf}: y={y_rbf_val:.4f}")

x_rbf_plot = np.linspace(1, 7, 100)
y_rbf_plot = rbf(x_rbf_plot)

plt.figure(figsize=(10, 6))
plt.plot(x_rbf, y_rbf, 'o', label='Исходные данные', markersize=8)
plt.plot(x_rbf_plot, y_rbf_plot, '-', label='RBF интерполяция', linewidth=2)
plt.plot(x_star_rbf, y_rbf_val, '*', markersize=12, label=f'Значение в x={x_star_rbf}')
plt.legend()
plt.grid(True)
plt.title('Задание 8: Радиальная базисная функция')
plt.show()