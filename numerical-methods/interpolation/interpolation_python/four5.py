from scipy import interpolate
import numpy as np
import scipy.linalg as linalg
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt


# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5

print("\n=== ЗАДАНИЕ 5 (стр. 87) ===")
# B-сплайны 2-й и 3-й степени

x_bspl = np.array([1, 2+nu/10, 3, 4, 5])
y_bspl = np.array([-2, 1, mu, 9, nu])

t2 = interpolate.splrep(x_bspl, y_bspl, k=2)
t3 = interpolate.splrep(x_bspl, y_bspl, k=3)

x_bspl_plot = np.linspace(1, 5, 100)
y_bspl2 = interpolate.splev(x_bspl_plot, t2)
y_bspl3 = interpolate.splev(x_bspl_plot, t3)

plt.figure(figsize=(10, 6))
plt.plot(x_bspl, y_bspl, 'o', label='Исходные данные', markersize=8)
plt.plot(x_bspl_plot, y_bspl2, '--', label='B-сплайн 2-й степени', linewidth=2)
plt.plot(x_bspl_plot, y_bspl3, '-', label='B-сплайн 3-й степени', linewidth=2)
plt.legend()
plt.grid(True)
plt.title('Задание 5: B-сплайны')
plt.show()