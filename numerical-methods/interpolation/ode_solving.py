import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5

print("\n=== ЗАДАНИЕ 1b (стр. 121) ===")
# ОДУ: x*y' = y + x^2*cos(x), y(x0) = y0

# Вычисление начальных условий
x0_1b = 0.5 * (mu + theta + 1)  # x0 = 0.5*(0+2+1) = 1.5
y0_1b = (nu + gamma) / 2 if (nu + gamma) != 0 else 1.0  # y0 = (5+1)/2 = 3.0

print(f"Начальные условия: x0={x0_1b}, y0={y0_1b}")

# Определение параметров для численного решения
h_1a = 0.1  # шаг интегрирования
n_steps_1a = 3  # количество шагов

def f_1b(x, y):
    """Правая часть ОДУ: dy/dx = (y + x^2*cos(x))/x"""
    # Для x=0 используем предельное значение, избегаем деления на ноль
    if abs(x) < 1e-12:
        # При x→0: dy/dx = x*cos(x) → 0
        return 0.0
    return (y + x**2 * np.cos(x)) / x

def runge_kutta_step(f, x, y, h):
    """Один шаг метода Рунге-Кутта 4-го порядка"""
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6

# ========== МЕТОД ЭЙЛЕРА ==========
x_euler_b = [x0_1b]
y_euler_b = [y0_1b]

for i in range(n_steps_1a):
    x_current = x_euler_b[-1]
    y_current = y_euler_b[-1]
    
    # Вычисление новой точки
    x_new = x_current + h_1a
    y_new = y_current + h_1a * f_1b(x_current, y_current)
    
    x_euler_b.append(x_new)
    y_euler_b.append(y_new)

print("\nМетод Эйлера:")
for i, (x, y) in enumerate(zip(x_euler_b, y_euler_b)):
    print(f"  Шаг {i}: x={x:.2f}, y={y:.6f}")

# ========== МЕТОД РУНГЕ-КУТТА ==========
x_rk_b = [x0_1b]
y_rk_b = [y0_1b]

for i in range(n_steps_1a):
    x_current = x_rk_b[-1]
    y_current = y_rk_b[-1]
    
    x_new = x_current + h_1a
    y_new = runge_kutta_step(f_1b, x_current, y_current, h_1a)
    
    x_rk_b.append(x_new)
    y_rk_b.append(y_new)

print("\nМетод Рунге-Кутта:")
for i, (x, y) in enumerate(zip(x_rk_b, y_rk_b)):
    print(f"  Шаг {i}: x={x:.2f}, y={y:.6f}")

# ========== РЕШЕНИЕ С solve_ivp ==========
x_span_b = (x0_1b, x0_1b + n_steps_1a * h_1a)  # интервал от x0 до x0+1.0
x_eval_b = np.linspace(x0_1b, x0_1b + n_steps_1a * h_1a, n_steps_1a + 1)

# Оборачиваем функцию для solve_ivp (требует векторный формат)
def f_ivp(x, y):
    return [f_1b(x, y[0])]

sol_1b = solve_ivp(f_ivp, x_span_b, [y0_1b], t_eval=x_eval_b, method='RK45')

print("\nМетод solve_ivp (RK45):")
for i, (x, y) in enumerate(zip(sol_1b.t, sol_1b.y[0])):
    print(f"  Шаг {i}: x={x:.2f}, y={y:.6f}")

# ========== ВИЗУАЛИЗАЦИЯ РЕЗУЛЬТАТОВ ==========
plt.figure(figsize=(12, 8))
plt.plot(x_euler_b, y_euler_b, 'o-', label='Метод Эйлера', markersize=6, linewidth=1.5)
plt.plot(x_rk_b, y_rk_b, 's-', label='Метод Рунге-Кутта 4-го порядка', markersize=6, linewidth=1.5)
plt.plot(sol_1b.t, sol_1b.y[0], '^-', label='solve_ivp (RK45)', markersize=6, linewidth=2)

plt.axvline(x=x0_1b, color='red', linestyle='--', alpha=0.7, label=f'Начальная точка x₀={x0_1b}')
plt.axhline(y=y0_1b, color='red', linestyle='--', alpha=0.7, label=f'Начальное значение y₀={y0_1b}')

plt.legend()
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Задание 1b: Решение ОДУ x·y′ = y + x²·cos(x)')
plt.show()

# ========== СРАВНЕНИЕ МЕТОДОВ ==========
print("\nСравнение методов на последнем шаге:")
print(f"Метод Эйлера: y({x_euler_b[-1]:.2f}) = {y_euler_b[-1]:.6f}")
print(f"Метод Рунге-Кутта: y({x_rk_b[-1]:.2f}) = {y_rk_b[-1]:.6f}")
print(f"Метод solve_ivp: y({sol_1b.t[-1]:.2f}) = {sol_1b.y[0][-1]:.6f}")