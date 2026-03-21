from scipy import interpolate
import numpy as np
import scipy.linalg as linalg
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt


# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5

print("\n=== ЗАДАНИЕ 7 (стр. 87) ===")
# Корни B-сплайна

x_root = np.array([1, 2, 3, 5])
y_root = np.array([-6, mu, nu, -6])

t_root = interpolate.splrep(x_root, y_root, k=3)
roots = interpolate.sproot(t_root)

print(f"Корни сплайна: {roots}")

x_root_plot = np.linspace(1, 5, 100)
y_root_plot = interpolate.splev(x_root_plot, t_root)

plt.figure(figsize=(10, 6))
plt.plot(x_root, y_root, 'o', label='Исходные данные', markersize=8)
plt.plot(x_root_plot, y_root_plot, '-', label='B-сплайн', linewidth=2)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
if len(roots) > 0:
    plt.plot(roots, np.zeros_like(roots), '*r', markersize=12, label='Корни')
plt.legend()
plt.grid(True)
plt.title('Задание 7: Корни B-сплайна')
plt.show()