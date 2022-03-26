# Задание 2
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

import timeit
import cProfile
import math


def if_simple(some_numb):
    if some_numb == 2:
        return True
    if some_numb % 2 == 0:
        return False
    for i in range(3, some_numb):
        if some_numb % i == 0:
            return False
    return True


def prime(data):
    if data == 0:
        return 'Ошибка ввода'
    result = 2
    j = 1
    while j != data:
        result += 1
        if if_simple(result):
            j += 1
    return result


def sieve(i):
    result = 'ошибка ввода'
    if i == 1:
        return 2
    count = 1
    i_max = prime_counting_function(i)  # нашли максимальную (теоретически) длинну списка для i-го натурального
    spam_set = set()
    spam_set.update(_ for _ in range(3, i_max + 1, 2))  # сформировали множество. будущее решето. уже без четных
    while i > count:
        result = min(spam_set)
        # уменьшили множество на множество с шагом минимального значения
        spam_set = spam_set - set(_ for _ in range(result, i_max + 1, result))
        count += 1
    return result


def prime_counting_function(i):
    """
    Долго не мог придумать как создать множество достаточное для решета. Эту функцию нагуглил.
    Количество простых чисел на отрезке [1;n] растёт с увеличением n как n / ln(n).
    """
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


n = 25

print(f'Дан номер простого числа n = {n}')
print('-' * 45)

print('Решение.')
max_column = 5
atmpts = 100  # кол-во замеров
rounding = 10  # округление результатов замеров

print('Функция с "Решето" - sieve')
print('Функция с "С обычной проверкой" - prime')
print(f'Попыток на каждый случай: {atmpts}')
print('-' * 45)

matrix = [['Название функции']]
for i in range(1, 3):
    matrix.append([])
    for j in range(2, max_column + 2):
        n, spam = n * j, n
        if i == 1:
            el = round(timeit.timeit(f'sieve({n})', number=atmpts, globals=globals()), rounding)
            matrix[i].append(el)
        if i == 2:
            el = round(timeit.timeit(f'prime({n})', number=atmpts, globals=globals()), rounding)
            matrix[i].append(el)
        if len(matrix[0]) <= max_column:
            matrix[0].append(f'n*{j}')
        n = spam

matrix[1].insert(0, f'sieve')
matrix[2].insert(0, f'prime')


for el in matrix:
    for i in el:
        print(f'|{i:^16}|', end=' ')
    print('\n', '-' * (max_column * 22))

"""
Дан номер простого числа n = 25
---------------------------------------------
Решение.
Функция с "Решето" - sieve
Функция с "С обычной проверкой" - prime
Попыток на каждый случай: 100
---------------------------------------------
|Название функции| |      n*2       | |      n*3       | |      n*4       | |      n*5       | |      n*6       | 
 --------------------------------------------------------------------------------------------------------------
|     sieve      | |   0.0223006    | |   0.0478515    | |   0.0637621    | |   0.0810412    | |   0.1038003    | 
 --------------------------------------------------------------------------------------------------------------
|     prime      | |   0.0254401    | |   0.0615345    | |   0.1169594    | |    0.208577    | |   0.3058936    | 
 --------------------------------------------------------------------------------------------------------------

очевидно что решето работает лучше. И чем больше n тем разница заметнее.
"""

cProfile.run('sieve(n*50)')
cProfile.run('prime(n*50)')

"""
Проверка на простое число функцией if_simple 10175 раз занимает почти все 100% времени работы ункции prime.
В тоже время множества в функции sieve работают прямо мнгновенно.
"""