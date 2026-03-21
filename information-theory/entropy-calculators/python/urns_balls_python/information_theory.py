import math

# Функция для вычисления энтропии
def entropy(probabilities):
    return sum(p * math.log2(1 / p) for p in probabilities if p > 0)

# Количество шаров (задаем количество для каждого цвета)
balls = {"white": 10, "blue": 10, "red": 1}

# Общее количество шаров
total_balls = sum(balls.values())

# Вычисляем вероятности для каждого цвета
probabilities = {color: count / total_balls for color, count in balls.items()}

# Выводим вероятности каждого цвета
print("Вероятности для каждого цвета:")
for color, prob in probabilities.items():
    print(f"{color}: {prob:.4f}")

# Вычисляем энтропию
urn_entropy = entropy(probabilities.values())

# Вывод энтропии
print(f"\nЭнтропия: {urn_entropy:.4f}")
