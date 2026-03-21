from scipy import interpolate
import numpy as np
import scipy.linalg as linalg
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5

print("\n=== ЗАДАНИЕ 4 (стр. 87) ===")
# Интерполяция с помощью interp1d

x_int4 = np.array([1, 2+mu/(nu+1), 6, 7])
y_int4 = np.array([-1, 6, 18, mu])

f_quad = interpolate.interp1d(x_int4, y_int4, kind='quadratic')
f_cubic = interpolate.interp1d(x_int4, y_int4, kind='cubic')

x_star4 = [3.4, 4.4]
for xs in x_star4:
    print(f"y({xs}) квадратичная: {f_quad(xs):.4f}")
    print(f"y({xs}) кубическая: {f_cubic(xs):.4f}")

x_plot4 = np.linspace(x_int4.min(), x_int4.max(), 100)
plt.figure(figsize=(10, 6))
plt.plot(x_int4, y_int4, 'o', label='Исходные данные', markersize=8)
plt.plot(x_plot4, f_quad(x_plot4), '-', label='Квадратичная', linewidth=2)
plt.plot(x_plot4, f_cubic(x_plot4), '--', label='Кубическая', linewidth=2)
plt.plot(x_star4, [f_quad(x) for x in x_star4], '*', markersize=12, label='Вычисленные точки')
plt.legend()
plt.grid(True)
plt.title('Задание 4: Интерполяция')
plt.show()