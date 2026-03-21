class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

def find_next_greater(arr):
    """
    Алгоритм поиска ближайшего большего элемента за O(n).
    """
    n = len(arr)
    result = [0] * n
    stack = Stack()

    for i in range(n):
        while not stack.is_empty() and arr[i] > arr[stack.peek()]:
            prev_index = stack.pop()
            result[prev_index] = arr[i]
        stack.push(i)
    
    return result

if __name__ == "__main__":
    print("Задание 3: Поиск ближайшего большего элемента")
    print("Введите последовательность чисел через пробел (например: 1 3 2 5 4):")
    
    user_input = input(">>> ").strip()
    
    if not user_input:
        print("Ошибка: введена пустая строка.")
    else:
        try:
            # Превращаем строку в список целых чисел
            # split() разбивает по пробелам, int() конвертирует
            A = [int(x) for x in user_input.split()]
            
            print(f"\nИсходная последовательность: {user_input}")
            
            res = find_next_greater(A)
            
            # Красивый вывод результата через пробел
            print(f"Результат замены: {' '.join(map(str, res))}")
            
        except ValueError:
            print("Ошибка: вводите только целые числа, разделенные пробелами.")