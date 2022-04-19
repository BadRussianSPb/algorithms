# Задание 2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import random


def my_marge_sort(some_arr):
    """
    Собственная реализация сортировки слиянием.
    """
    if len(some_arr) > 1:
        middle = len(some_arr) // 2
        left_arr = some_arr[:middle]
        right_arr = some_arr[middle:]  # !!!
        my_marge_sort(left_arr)
        my_marge_sort(right_arr)
        i = j = k = 0  # i - left, j - right, k - some_arr

        # цикл пока не переберем все значения массивов
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                some_arr[k] = left_arr[i]
                i += 1
            else:
                some_arr[k] = right_arr[j]
                j += 1
            k += 1

        # циклы на случай если один массив "закончислся" раньше другого.
        while i < len(left_arr):
            some_arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            some_arr[k] = right_arr[j]
            j += 1
            k += 1
    return some_arr


if __name__ == '__main__':

    MAX_RANGE = 50.0
    SIZE = 10

    some_data = [random()*MAX_RANGE for x in range(SIZE)]

    print('Дано:', '\n', some_data)
    print('Результат:', '\n', my_marge_sort(some_data))
