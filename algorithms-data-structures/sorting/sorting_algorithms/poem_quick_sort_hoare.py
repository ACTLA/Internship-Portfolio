# 1. Создаем список из стихов одного автора 
poems = [
    "Я помню чудное мгновенье:\nПередо мной явилась ты,\nКак мимолетное виденье,\nКак гений чистой красоты.",
    "Мороз и солнце; день чудесный!\nЕще ты дремлешь, друг прелестный —\nПора, красавица, проснись...",
    "Буря мглою небо кроет,\nВихри снежные крутя;\nТо, как зверь, она завоет,\nТо заплачет, как дитя.",
    "Я памятник себе воздвиг нерукотворный,\nК нему не зарастет народная тропа..."
]

import random

def quick_sort_inplace(arr, low, high):
    if low < high:
        # Получаем индекс разделителя
        p_index = partition(arr, low, high)
        # Сортируем элементы до и после разделителя
        quick_sort_inplace(arr, low, p_index)
        quick_sort_inplace(arr, p_index + 1, high)

def partition(arr, low, high):
    # Оптимизация: выбираем случайный pivot и меняем его с центральным
    pivot_idx = random.randint(low, high)
    pivot_len = len(arr[pivot_idx])
    
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while len(arr[i]) < pivot_len: i += 1
        j -= 1
        while len(arr[j]) > pivot_len: j -= 1
        
        if i >= j:
            return j
        # Меняем элементы местами без создания новых списков
        arr[i], arr[j] = arr[j], arr[i]

# Вызов для твоего списка:
quick_sort_inplace(poems, 0, len(poems) - 1)

# Вывод результата 
print("Список стихов, отсортированный по возрастанию размера:")
for poem in poems:
    print(f"--- Размер: {len(poem)} символов ---")
    print(poem)
    print()