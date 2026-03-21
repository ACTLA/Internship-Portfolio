import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5

print("\n=== ЗАДАНИЕ 2 (стр. 121) ===")
# Система ОДУ: y' = N_ст*y + cos(z), z' = sin(y) + N_ст*x*z

# Используем mu как номер студента по списку (если mu=0, берем 1 для избежания нуля)
N_st = mu if mu != 0 else 1

def system_ode(t, s):
    """Система ОДУ: s = [y, z]"""
    y, z = s
    dydt = N_st * y + np.cos(z)
    dzdt = np.sin(y) + N_st * t * z
    return [dydt, dzdt]

# Параметры решения
t_span_2 = (0, 2)  # Уменьшим интервал для лучшей стабильности
t_eval_2 = np.linspace(0, 2, 21)  # 20 шагов с шагом 0.1
s0_2 = [1, 0.5]  # Начальные условия

print(f"Параметры решения:")
print(f"N_st = {N_st}")
print(f"Интервал t: {t_span_2}")
print(f"Начальные условия: y0={s0_2[0]}, z0={s0_2[1]}")

# Решение с помощью odeint
sol_odeint = odeint(lambda s, t: system_ode(t, s), s0_2, t_eval_2)

# Решение с помощью solve_ivp для сравнения
sol_ivp = solve_ivp(system_ode, t_span_2, s0_2, t_eval=t_eval_2, method='RK45')

print("\nРешение системы ОДУ (первые 5 точек):")
print("t       y(t)           z(t)")
for i in range(min(5, len(t_eval_2))):
    print(f"{t_eval_2[i]:.1f}   {sol_odeint[i, 0]:.6f}   {sol_odeint[i, 1]:.6f}")

# Визуализация результатов
plt.figure(figsize=(14, 5))

# График решений по времени
plt.subplot(1, 2, 1)
plt.plot(t_eval_2, sol_odeint[:, 0], 'o-', label='y(t) - odeint', markersize=4, linewidth=1.5)
plt.plot(t_eval_2, sol_odeint[:, 1], 's-', label='z(t) - odeint', markersize=4, linewidth=1.5)
plt.plot(sol_ivp.t, sol_ivp.y[0], '--', label='y(t) - solve_ivp', linewidth=1.5)
plt.plot(sol_ivp.t, sol_ivp.y[1], '--', label='z(t) - solve_ivp', linewidth=1.5)
plt.xlabel('t')
plt.ylabel('y(t), z(t)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.title('Решение системы ОДУ')

# Фазовая плоскость
plt.subplot(1, 2, 2)
plt.plot(sol_odeint[:, 0], sol_odeint[:, 1], 'o-', markersize=4, linewidth=1.5, label='odeint')
plt.plot(sol_ivp.y[0], sol_ivp.y[1], '--', linewidth=1.5, label='solve_ivp')
plt.xlabel('y')
plt.ylabel('z')
plt.grid(True, alpha=0.3)
plt.legend()
plt.title('Фазовая плоскость y-z')

plt.tight_layout()
plt.show()

# Сравнение методов
print("\nСравнение методов на последней точке:")
print(f"odeint:     y({t_eval_2[-1]:.1f}) = {sol_odeint[-1, 0]:.6f}, z({t_eval_2[-1]:.1f}) = {sol_odeint[-1, 1]:.6f}")
print(f"solve_ivp:  y({sol_ivp.t[-1]:.1f}) = {sol_ivp.y[0, -1]:.6f}, z({sol_ivp.t[-1]:.1f}) = {sol_ivp.y[1, -1]:.6f}")