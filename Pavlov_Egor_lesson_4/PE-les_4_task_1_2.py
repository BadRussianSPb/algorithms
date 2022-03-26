# Задание 1 Вариант 2
# Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.

# здесь рассмотрено 6-е задание из 3-го урока. Без функций min и max, с ними и индексами, и с ними и без индексов
# # В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import cProfile
import random
import timeit


def new_arrey(n):
    array_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(n)]
    return array_


def get_min_max_v1(data):
    array_ = new_arrey(data)
    min_el = max_el = array_[0]
    min_idx = 0

    for el in array_:
        if el < min_el:  # <= даст последнее вхождение минимального элемента
            min_el, min_idx = el, array_.index(el)
        if el > max_el:  # <= даст последнее вхождение максимального элемента
            max_el, max_idx = el, array_.index(el)
            array_[min_idx], array_[max_idx] = max_el, min_el
    return array_


def get_min_max_v2(data):
    array_ = new_arrey(data)
    min_el = max_el = array_[0]
    min_idx = 0

    for i in range(len(array_)):
        if array_[i] < min_el:  # <= даст последнее вхождение минимального элемента
            min_el, min_idx = array_[i], i
        if array_[i] > max_el:  # <= даст последнее вхождение максимального элемента
            max_el, max_idx = array_[i], i
            array_[min_idx], array_[max_idx] = max_el, min_el
    return array_


def get_min_max_v3(data):
    array_ = new_arrey(data)
    min_el = min(array_)
    max_el = max(array_)
    min_idx = array_.index(min_el)
    max_idx = array_.index(max_el)
    array_[min_idx], array_[max_idx] = max_el, min_el
    return array_


RANGE_MIN = -10
RANGE_MAX = 10
max_column = 5
n = 250

print(f'Дан массив с длинной n = {n}')
print('-' * 45)

print('Решение.')
atmpts = 100  # кол-во замеров
rounding = 10  # округление результатов замеров

print('Функция с "Циклом по элементам" - from_the_end_v1')
print('Функция с "Циклом по индексам" - from_the_end_v2')
print('Функция с "Функции min и max"- from_the_end_v3')
print(f'Попыток на каждый случай: {atmpts}')
print('-' * 45)

matrix = [['Название функции']]
for i in range(1, 4):
    matrix.append([])
    matrix[i].append(f'from_the_end_v{i}')
    for j in range(2, max_column + 2):
        n, spam = n * j, n
        el = round(timeit.timeit(f'get_min_max_v{i}({n})', number=atmpts, globals=globals()), rounding)
        matrix[i].append(el)
        if len(matrix[0]) <= max_column:
            matrix[0].append(f'n*{j}')
        n = spam
for el in matrix:
    for i in el:
        print(f'|{i:^16}|', end=' ')
    print('\n', '-' * (max_column * 22))

"""
Дан массив с длинной n = 250
---------------------------------------------
Решение.
Функция с "Циклом по элементам" - from_the_end_v1
Функция с "Циклом по индексам" - from_the_end_v2
Функция с "Функции min и max"- from_the_end_v3
Попыток на каждый случай: 100
---------------------------------------------
|Название функции| |      n*2       | |      n*3       | |      n*4       | |      n*5       | |      n*6       | 
 --------------------------------------------------------------------------------------------------------------
|from_the_end_v1 | |   0.0452702    | |   0.0584066    | |   0.0883614    | |    0.094278    | |   0.1305523    | 
 --------------------------------------------------------------------------------------------------------------
|from_the_end_v2 | |   0.0404982    | |   0.0621415    | |   0.0790918    | |    0.102222    | |   0.1829626    | 
 --------------------------------------------------------------------------------------------------------------
|from_the_end_v3 | |   0.0396842    | |   0.0553635    | |   0.0904447    | |   0.1382572    | |    0.171945    | 
 --------------------------------------------------------------------------------------------------------------
 
много раз "прогонял" с разной длинной массивов и есть подозрения, что первая функция на бОльших длиннах массивов
начинает работать быстрее чем другие функции. Не всегда, но в 3 из 5 случаях похоже на то.
и второе наблюдение, что функции min и max никакой заметной прибавки к скорости не дают.
"""

cProfile.run('get_min_max_v1(n*600)')
cProfile.run('get_min_max_v2(n*600)')
cProfile.run('get_min_max_v3(n*600)')

"""
самые большие затраты по времени у всех функци это само создание массива
{method 'index' of 'list' objects} был вызван 8 раз в первом варианте против 2 раз в третьем
"""
