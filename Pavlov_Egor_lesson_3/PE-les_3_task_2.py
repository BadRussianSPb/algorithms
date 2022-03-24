# Задание 2
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random


def even_idx(given, result=None, count=0):
    if result is None:
        result = []
    while count < len(given):
        if given[count] % 2 == 0:
            result.append(count)
        return even_idx(given, result, count + 1)
    return result


# постановка задачи

SIZE = 20
RANGE_MIN = -100
RANGE_MAX = 100

array_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(SIZE)]
print('Дано')
print(array_)
print('-' * 45)

# решение

print('Вариант с рекурсией.')
print(even_idx(array_))

# ---------------------------------------------------------------------------------
print('-' * 45)

print('Вариант с простым циклом.')

result_list = []
result_dict = {}
result_set = set()

for i in range(len(array_)):
    if array_[i] % 2 == 0:
        result_list.append(i)
        # задание практическое же. Вот и практикуюсь.
        result_dict[i] = array_[i]  # наоборот не вариант т.к. значения могут повторяться
        result_set.add(i)

print('Список', result_list)
print('Множество', result_set)
print('Словарь', result_dict)
