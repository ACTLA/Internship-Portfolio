from scipy import interpolate
import numpy as np
import scipy.linalg as linalg
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt


# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5


print("\n=== ЗАДАНИЕ 6 (стр. 87) ===")
# Кубические B-сплайны с вычислением значений и производных

x_bspl6 = np.array([1, 2, 4, 5, 7])
y_bspl6 = np.array([0, 1, 15+nu, mu, 8])

t_bspl6 = interpolate.splrep(x_bspl6, y_bspl6, k=3)

x_star6 = [1.5, 8.5]
for xs in x_star6:
    if x_bspl6.min() <= xs <= x_bspl6.max():
        y_val = interpolate.splev(xs, t_bspl6, der=0)
        y_der1 = interpolate.splev(xs, t_bspl6, der=1)
        y_der2 = interpolate.splev(xs, t_bspl6, der=2)
        print(f"В точке x={xs}: y={y_val:.4f}, y'={y_der1:.4f}, y''={y_der2:.4f}")
    else:
        # Экстраполяция
        y_val = interpolate.splev(xs, t_bspl6, der=0, ext=0)
        print(f"В точке x={xs} (экстраполяция): y={y_val:.4f}")

x_plot6 = np.linspace(0.5, 8.5, 200)
y_plot6 = interpolate.splev(x_plot6, t_bspl6, ext=0)

plt.figure(figsize=(10, 6))
plt.plot(x_bspl6, y_bspl6, 'o', label='Исходные данные', markersize=8)
plt.plot(x_plot6, y_plot6, '-', label='Кубический B-сплайн', linewidth=2)
plt.plot(x_star6, [interpolate.splev(x, t_bspl6, ext=0) for x in x_star6], '*', 
         markersize=12, label='Вычисленные точки')
plt.legend()
plt.grid(True)
plt.title('Задание 6: Кубические B-сплайны')
plt.show()