from scipy import integrate
import numpy as np

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 3, 1, 8

print("\n=== ЗАДАНИЕ 2 (стр. 104) ===")
# Программа для вычисления интеграла тремя методами

def rectangle_rule(f, a, b, n):
    """Метод прямоугольников (средних точек)"""
    h = (b - a) / n
    x = np.linspace(a + h/2, b - h/2, n)
    return h * np.sum(f(x))

def trapezoid_rule(f, a, b, n):
    """Метод трапеций"""
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h * (y[0]/2 + np.sum(y[1:-1]) + y[-1]/2)

def simpson_rule(f, a, b, n):
    """Метод Симпсона"""
    if n % 2 == 1:
        n += 1
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    return h/3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])

# Используем интеграл из задания 1a с вашими параметрами
f_test = lambda x: np.exp(((x-nu)**2)/8)
a_test = nu + 0.2 * mu - 1
b_test = 2 + 1.3 * nu
n_test = 10

# print(f"Пределы интегрирования: от {a_test} до {b_test}")
# print(f"Функция: exp(((x-{nu})**2)/8)")

I_rect = rectangle_rule(f_test, a_test, b_test, n_test)
I_trap = trapezoid_rule(f_test, a_test, b_test, n_test)
I_simp = simpson_rule(f_test, a_test, b_test, n_test)
I_exact, _ = integrate.quad(f_test, a_test, b_test)

print(f"Метод прямоугольников: {I_rect:.8f}, ошибка: {abs(I_rect - I_exact):.2e}")
print(f"Метод трапеций: {I_trap:.8f}, ошибка: {abs(I_trap - I_exact):.2e}")
print(f"Метод Симпсона: {I_simp:.8f}, ошибка: {abs(I_simp - I_exact):.2e}")
print(f"Точное значение (quad): {I_exact:.8f}")