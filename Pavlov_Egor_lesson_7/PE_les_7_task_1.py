# Задание 1
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.

from random import randint


def my_bubble_sort(some_arr):
    """
    Собственная реализация пузырьковой сортировки.
    """
    not_ordered = True
    it_numb = 0
    while not_ordered:
        not_ordered = False  # если флаг остенется неизменным - список отсортирован. можно делать 'return'
        for i in range(len(some_arr) - it_numb - 1):  # '-it_numb' учитываем, что i-й с конца элемент на своем месте
            if some_arr[i] > some_arr[i + 1]:
                some_arr[i], some_arr[i + 1] = some_arr[i + 1], some_arr[i]
                not_ordered = True
        it_numb += 1
    print(f'Итераций {it_numb} из {len(some_arr)} возможных.')
    return some_arr


if __name__ == '__main__':

    MIN_RANGE = -100
    MAX_RANGE = 100
    SIZE = 10

    some_data = [randint(MIN_RANGE, MAX_RANGE - 1) for x in range(SIZE)]

    print('Дано:', some_data)
    print('Результат:', my_bubble_sort(some_data))
