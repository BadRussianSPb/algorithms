# Задание 6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 20
RANGE_MIN = -10
RANGE_MAX = 10

array_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(SIZE)]
print('Дано')
print(array_)
print('-' * 45)

# решение
print('Решение.')
# первая часть решения это 3-е задание.
min_el = max_el = array_[0]
min_idx = max_idx = 0
result_sum = 0

for i, el in enumerate(array_):
    if el < min_el:  # <= даст последнее вхождение минимального элемента
        min_el, min_idx = el, i
    if el > max_el:  # <= даст последнее вхождение максимального элемента
        max_el, max_idx = el, i

# вторая часть решения с подсчетом суммы
if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx  # дабы сработал цикл ниже
for i in range(min_idx + 1, max_idx):
    result_sum += array_[i]

print(f'Минимальное значение "{min_el}" и Максимальное значение "{max_el}". Индексы "{min_idx}" и "{max_idx}"')
print(f'Сумма элементов между максимальным и минимальным значениями: {result_sum}')
