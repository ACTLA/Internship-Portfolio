# 1. Список стихов одного автора
poems = [
    "Я помню чудное мгновенье:\nПередо мной явилась ты,\nКак мимолетное виденье,\nКак гений чистой красоты.",
    "Мороз и солнце; день чудесный!\nЕще ты дремлешь, друг прелестный —\nПора, красавица, проснись...",
    "Буря мглою небо кроет,\nВихри снежные крутя;\nТо, как зверь, она завоет,\nТо заплачет, как дитя.",
    "Я памятник себе воздвиг нерукотворный,\nК нему не зарастет народная тропа..."
]

def merge_sort_by_length(arr):
    """
    Рекурсивная функция сортировки слиянием.
    """
    # Базовый случай: если в массиве 0 или 1 элемент, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Находим середину массива и разделяем его на две части
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно вызываем сортировку для каждой половины
    left_sorted = merge_sort_by_length(left_half)
    right_sorted = merge_sort_by_length(right_half)

    # Сливаем две отсортированные половины в одну
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Вспомогательная функция для слияния двух отсортированных списков.
    """
    result = []
    i = j = 0

    # Сравниваем элементы левого и правого списков по их длине
    while i < len(left) and j < len(right):
        if len(left[i]) <= len(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Если в одном из списков остались элементы, добавляем их в конец результата
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Применяем сортировку
sorted_poems = merge_sort_by_length(poems)

# Вывод результата
print("Список стихов, отсортированный методом Merge Sort (по длине):")
print("-" * 50)
for poem in sorted_poems:
    print(f"[Длина: {len(poem)} симв.]")
    print(poem)
    print()