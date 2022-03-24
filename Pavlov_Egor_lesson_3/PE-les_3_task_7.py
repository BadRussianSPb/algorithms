# Задание 7
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 20
RANGE_MIN = -20
RANGE_MAX = 20

array_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(SIZE)]
print('Дано')
print(array_)
print('-' * 45)

# решение
print('Решение.')

min_1 = min_2 = array_[0]

for el in array_:
    if el <= min_1:
        min_2, min_1 = min_1, el

print(min_1, min_2)
