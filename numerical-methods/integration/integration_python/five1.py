from scipy import integrate
import numpy as np

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 3, 1, 8

print("\n=== ЗАДАНИЕ 1a (стр. 104) ===")

# Правильные пределы интегрирования согласно заданию
a1 = nu + 0.2 * mu - 1
b1 = 2 + 1.3 * nu

n_intervals = 10
x_int1a = np.linspace(a1, b1, n_intervals + 1)
y_int1a = np.exp(((x_int1a-nu)**2)/8)

# Формула трапеций
I_trapezoid = integrate.trapezoid(y_int1a, x_int1a)
print(f"Интеграл (метод трапеций): {I_trapezoid:.8f}")

# Формула Симпсона
I_simpson = integrate.simpson(y_int1a, x_int1a)
print(f"Интеграл (метод Симпсона): {I_simpson:.8f}")

# Для проверки точности - метод quad
I_quad, err = integrate.quad(lambda x: np.exp(((x-nu)**2)/8), a1, b1)
print(f"Интеграл (quad): {I_quad:.8f}")