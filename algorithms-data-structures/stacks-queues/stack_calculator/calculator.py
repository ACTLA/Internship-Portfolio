class Stack:
    """Реализация структуры данных Стек."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Извлечение из пустого стека")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def apply_op(operators, values):
    """Выполняет одну арифметическую операцию."""
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    
    if operator == '+': values.push(left + right)
    elif operator == '-': values.push(left - right)
    elif operator == '*': values.push(left * right)
    elif operator == '/':
        if right == 0:
            raise ZeroDivisionError("Деление на ноль")
        values.push(left / right)

def get_priority(op):
    """Определяет приоритет операторов."""
    if op in ('+', '-'): return 1
    if op in ('*', '/'): return 2
    return 0

def evaluate(expression):
    """Вычисляет значение арифметического выражения с помощью двух стеков."""
    values = Stack()    # Стек для чисел
    operators = Stack() # Стек для операторов
    
    # Удаляем пробелы
    expr = expression.replace(' ', '')
    i = 0
    
    try:
        while i < len(expr):
            # 1. Если символ — число, считываем его полностью
            if expr[i].isdigit():
                num = 0
                while i < len(expr) and expr[i].isdigit():
                    num = num * 10 + int(expr[i])
                    i += 1
                values.push(num)
                continue # Пропускаем i += 1 в конце цикла
            
            # 2. Обработка скобок
            elif expr[i] == '(':
                operators.push('(')
            
            elif expr[i] == ')':
                while not operators.is_empty() and operators.peek() != '(':
                    apply_op(operators, values)
                if operators.is_empty():
                    raise ValueError("Пропущена открывающая скобка")
                operators.pop() # Удаляем '('
            
            # 3. Обработка операторов (+, -, *, /)
            elif expr[i] in '+-*/':
                while (not operators.is_empty() and 
                       get_priority(operators.peek()) >= get_priority(expr[i])):
                    apply_op(operators, values)
                operators.push(expr[i])
            
            else:
                raise ValueError(f"Недопустимый символ: {expr[i]}")
            i += 1

        # Выполняем оставшиеся операции
        while not operators.is_empty():
            if operators.peek() == '(':
                raise ValueError("Пропущена закрывающая скобка")
            apply_op(operators, values)
            
        return values.pop()

    except Exception as e:
        # В случае ошибки выводим сообщение и само выражение 
        print(f"Ошибка: {e}")
        print(f"Введенное выражение: {expression}")
        return None

if __name__ == "__main__":
    # Запрос на ввод выражения 
    user_expr = input("Введите арифметическое выражение: ")
    result = evaluate(user_expr)
    
    if result is not None:
        # Вывод результата при корректном вводе 
        print(f"Результат: {result}")