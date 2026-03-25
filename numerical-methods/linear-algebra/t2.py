import numpy as np
import scipy.linalg as linalg
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5


print("\n=== ЗАДАНИЕ 2 (стр. 51) ===")
# Аппроксимация y = a*x^b

x = np.array([mu+nu, mu+nu+2, mu+nu+4, mu+nu+6])
y = np.array([gamma+theta+2.5, gamma+theta+4.9, gamma+theta+8, gamma+theta+12.1])

def power_func(x, a, b):
    return a * x**b

# Решение через curve_fit
popt_cf, _ = curve_fit(power_func, x, y, p0=[1, 1])
print(f"Коэффициенты (curve_fit): a={popt_cf[0]:.6f}, b={popt_cf[1]:.6f}")

# Решение через leastsq
def residuals_power(params, x, y):
    return y - power_func(x, *params)

popt_ls = leastsq(residuals_power, [1, 1], args=(x, y))[0]
print(f"Коэффициенты (leastsq): a={popt_ls[0]:.6f}, b={popt_ls[1]:.6f}")

x2_plot = np.linspace(x.min(), x.max(), 100)
y2_plot = power_func(x2_plot, *popt_cf)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Исходные данные', markersize=8)
plt.plot(x2_plot, y2_plot, '-', label=f'y = {popt_cf[0]:.3f}*x^{popt_cf[1]:.3f}', linewidth=2)
plt.legend()
plt.grid(True)
plt.title('Задание 2: Степенная аппроксимация')
plt.show()