# 1. Создаем список из стихов одного автора 
poems = [
    "Я помню чудное мгновенье:\nПередо мной явилась ты,\nКак мимолетное виденье,\nКак гений чистой красоты.",
    "Мороз и солнце; день чудесный!\nЕще ты дремлешь, друг прелестный —\nПора, красавица, проснись...",
    "Буря мглою небо кроет,\nВихри снежные крутя;\nТо, как зверь, она завоет,\nТо заплачет, как дитя.",
    "Я памятник себе воздвиг нерукотворный,\nК нему не зарастет народная тропа..."
]

# 2. Реализация алгоритма Quick Sort для сортировки по размеру 
def quick_sort_by_length(arr):
    if len(arr) <= 1:
        return arr
    
    # Выбираем опорный элемент (pivot) — возьмем средний
    pivot = arr[len(arr) // 2]
    pivot_len = len(pivot)
    
    # Разделяем список на три части: меньше, равные и больше опорного
    left = [x for x in arr if len(x) < pivot_len]
    middle = [x for x in arr if len(x) == pivot_len]
    right = [x for x in arr if len(x) > pivot_len]
    
    # Рекурсивно сортируем и объединяем
    return quick_sort_by_length(left) + middle + quick_sort_by_length(right)

# Применяем сортировку
sorted_poems = quick_sort_by_length(poems)

# Вывод результата 
print("Список стихов, отсортированный по возрастанию размера:")
for poem in sorted_poems:
    print(f"--- Размер: {len(poem)} символов ---")
    print(poem)
    print()