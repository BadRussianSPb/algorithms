# Задание 3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# постановка задачи
import random

SIZE = 20
RANGE_MIN = -50
RANGE_MAX = 50

array_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(SIZE)]
print('Дано')
print(array_)
print('-' * 45)

# решение

print('Решение. По первым вхождениям.')

min_el = max_el = array_[0]
min_idx = max_idx = 0
result_sum = 0

for i, el in enumerate(array_):
    if el < min_el:  # можно добавить знак = и замена будет по последним минимальным
        min_el, min_idx = el, i
    if el > max_el:  # можно добавить знак = и замена будет по последним максимальным
        max_el, max_idx = el, i

print(f'Минимальное значение "{min_el}" и Максимальное значение "{max_el}".'
      f' Индексы "{min_idx}" и "{max_idx}"')
array_[min_idx], array_[max_idx] = max_el, min_el  # поменяли местами значения по найденым индексам
print(array_)
