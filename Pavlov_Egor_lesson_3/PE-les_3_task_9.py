# Задание 9
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

MAX_COLUMN = 5
MAX_STR = 4
RANGE_MIN = 0
RANGE_MAX = 100

matrix = [[random.randint(RANGE_MIN, RANGE_MAX) for _ in range(MAX_COLUMN)] for _ in range(MAX_STR)]
print('Дано')
print(*matrix, sep='\n')
print('-' * 45)

print('Решение')
print('Минимальные по столбцам: ', end='')

max_el = RANGE_MIN - 1

for j in range(MAX_COLUMN):
    min_el = matrix[0][j]
    for i in range(MAX_STR):
        if matrix[i][j] < min_el:
            min_el = matrix[i][j]
    if max_el < min_el:
        max_el = min_el
    print(min_el, end=' ')
print()
print(f'Максимальное из минимальных: {max_el}')
