import numpy as np
import scipy.linalg as linalg
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5

print("=== ЗАДАНИЕ 1 (стр. 51) ===")
# Метод наименьших квадратов для параболы y = c0 + c1*x + c2*x^2

x = np.array([alpha, alpha+2, alpha+4, alpha+6, alpha+8])
y = np.array([mu+2.5, beta+4.9, nu+8, gamma+12.1, theta+16.9])

# Решение через систему нормальных уравнений
A_manual = np.array([
    [len(x), np.sum(x), np.sum(x**2)],
    [np.sum(x), np.sum(x**2), np.sum(x**3)],
    [np.sum(x**2), np.sum(x**3), np.sum(x**4)]
])
b_manual = np.array([np.sum(y), np.sum(x*y), np.sum(x**2*y)])
c_manual = np.linalg.solve(A_manual, b_manual)

print(f"Коэффициенты параболы (ручное решение): c0={c_manual[0]:.6f}, c1={c_manual[1]:.6f}, c2={c_manual[2]:.6f}")

# Решение через linalg.lstsq()
A_lstsq = np.column_stack([np.ones(len(x)), x, x**2])
c_lstsq, residuals, rank, s = linalg.lstsq(A_lstsq, y)
print(f"Коэффициенты параболы (lstsq): c0={c_lstsq[0]:.6f}, c1={c_lstsq[1]:.6f}, c2={c_lstsq[2]:.6f}")
print(f"Сумма квадратов отклонений: {residuals:.6f}")

# Аппроксимация y = a*b^x
def exp_func(x, a, b):
    return a * b**x

popt_exp, _ = curve_fit(exp_func, x, y, p0=[1, 1.1])
print(f"Коэффициенты экспоненты: a={popt_exp[0]:.6f}, b={popt_exp[1]:.6f}")

# Построение графиков
x_plot = np.linspace(x.min(), x.max(), 100)
y_parabola = c_lstsq[0] + c_lstsq[1]*x_plot + c_lstsq[2]*x_plot**2
y_exp = exp_func(x_plot, *popt_exp)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Исходные данные', markersize=8)
plt.plot(x_plot, y_parabola, '-', label='Парабола', linewidth=2)
plt.plot(x_plot, y_exp, '--', label='Экспонента', linewidth=2)
plt.legend()
plt.grid(True)
plt.title('Задание 1: Аппроксимация')
plt.show()