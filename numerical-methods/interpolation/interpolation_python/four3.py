import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt

# Параметры
alpha, beta, gamma, theta, mu, nu = 7, 3, 1, 2, 0, 5

print("\n=== ЗАДАНИЕ 3 (стр. 87) ===")
# Два кубических сплайна

x_spl = np.array([1, 2, 4])
y_spl = np.array([4, nu, 25+mu])
print(f"Исходные точки: x={x_spl}, y={y_spl}")

# ПРАВИЛЬНАЯ система для двух кубических сплайнов
# S1(x) = a0 + a1*x + a2*x^2 + a3*x^3 на [1,2]
# S2(x) = b0 + b1*x + b2*x^2 + b3*x^3 на [2,4]

A_spl = np.array([
    # S1(x0) = y0
    [1, 1, 1, 1, 0, 0, 0, 0],
    # S1(x1) = y1  
    [1, 2, 4, 8, 0, 0, 0, 0],
    # S2(x1) = y1
    [0, 0, 0, 0, 1, 2, 4, 8],
    # S2(x2) = y2
    [0, 0, 0, 0, 1, 4, 16, 64],
    # S1'(x1) = S2'(x1) - первые производные
    [0, 1, 4, 12, 0, -1, -4, -12],
    # S1''(x1) = S2''(x1) - вторые производные
    [0, 0, 2, 12, 0, 0, -2, -12],
    # S1''(x0) = 0 - вторая производная в начале
    [0, 0, 2, 6, 0, 0, 0, 0],
    # S2''(x2) = 0 - вторая производная в конце
    [0, 0, 0, 0, 0, 0, 2, 24]
])

b_spl = np.array([y_spl[0], y_spl[1], y_spl[1], y_spl[2], 0, 0, 0, 0])

try:
    coef_spl = np.linalg.solve(A_spl, b_spl)
    
    # Разделяем коэффициенты
    a0, a1, a2, a3, b0, b1, b2, b3 = coef_spl
    
    print(f"S1(x) = {a0:.4f} + {a1:.4f}*x + {a2:.4f}*x^2 + {a3:.4f}*x^3")
    print(f"S2(x) = {b0:.4f} + {b1:.4f}*x + {b2:.4f}*x^2 + {b3:.4f}*x^3")
    
    # Построение графиков
    x1_plot = np.linspace(1, 2, 100)
    x2_plot = np.linspace(2, 4, 100)
    
    # Вычисление значений сплайнов
    S1 = a0 + a1*x1_plot + a2*x1_plot**2 + a3*x1_plot**3
    S2 = b0 + b1*x2_plot + b2*x2_plot**2 + b3*x2_plot**3
    
    plt.figure(figsize=(12, 8))
    
    # Графики сплайнов
    plt.plot(x1_plot, S1, 'b-', linewidth=3, label='S1(x) на [1,2]')
    plt.plot(x2_plot, S2, 'r-', linewidth=3, label='S2(x) на [2,4]')
    
    # Исходные точки
    plt.plot(x_spl, y_spl, 'ko', markersize=10, label='Исходные точки', markerfacecolor='yellow')
    
    # Вертикальная линия в точке соединения
    plt.axvline(x=2, color='gray', linestyle='--', alpha=0.7, label='Точка соединения x=2')
    
    # Проверка соединения в точке x=2
    S1_x2 = a0 + a1*2 + a2*4 + a3*8
    S2_x2 = b0 + b1*2 + b2*4 + b3*8
    plt.plot(2, S1_x2, 'go', markersize=8, label=f'S1(2) = {S1_x2:.6f}')
    plt.plot(2, S2_x2, 'mo', markersize=8, label=f'S2(2) = {S2_x2:.6f}')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Два кубических сплайна через три точки (исправленная система)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    # # Детальная проверка условий
    # print("\n=== ПРОВЕРКА УСЛОВИЙ ===")
    
    # # Значения в узловых точках
    # print("Значения в узловых точках:")
    # print(f"S1(1) = {a0 + a1*1 + a2*1 + a3*1:.6f} (должно быть {y_spl[0]})")
    # print(f"S1(2) = {a0 + a1*2 + a2*4 + a3*8:.6f} (должно быть {y_spl[1]})")
    # print(f"S2(2) = {b0 + b1*2 + b2*4 + b3*8:.6f} (должно быть {y_spl[1]})")
    # print(f"S2(4) = {b0 + b1*4 + b2*16 + b3*64:.6f} (должно быть {y_spl[2]})")
    
    # # Производные в точке соединения
    # print("\nПроизводные в точке x=2:")
    # S1_prime_2 = a1 + 2*a2*2 + 3*a3*4
    # S2_prime_2 = b1 + 2*b2*2 + 3*b3*4
    # print(f"S1'(2) = {S1_prime_2:.6f}")
    # print(f"S2'(2) = {S2_prime_2:.6f}")
    # print(f"Разность первых производных: {abs(S1_prime_2 - S2_prime_2):.6e}")
    
    # # Вторые производные
    # print("\nВторые производные:")
    # S1_double_2 = 2*a2 + 6*a3*2
    # S2_double_2 = 2*b2 + 6*b3*2
    # print(f"S1''(2) = {S1_double_2:.6f}")
    # print(f"S2''(2) = {S2_double_2:.6f}")
    # print(f"Разность вторых производных: {abs(S1_double_2 - S2_double_2):.6e}")
    
    # # Граничные условия
    # print("\nГраничные условия:")
    # S1_double_1 = 2*a2 + 6*a3*1
    # S2_double_4 = 2*b2 + 6*b3*4
    # print(f"S1''(1) = {S1_double_1:.6f} (должно быть 0)")
    # print(f"S2''(4) = {S2_double_4:.6f} (должно быть 0)")
    
except np.linalg.LinAlgError as e:
    print(f"Ошибка решения системы: {e}")
    print("Матрица вырождена или плохо обусловлена")