# Задание 3
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).


from random import randint
from timeit import timeit
import PE_les_7_task_2


def my_median(some_arr):
    """
    Поиск медианного значения простым перебором и сравнением.
    """
    for i in range(len(some_arr)):
        less = 0
        equal = 1

        # я надеюсь цикл в цикле не считается методом пузырька?
        for j in range(len(some_arr)):
            if some_arr[i] > some_arr[j]:
                less += 1
            else:
                if some_arr[i] == some_arr[j]:
                    equal += 1

        # если ВСЕ значения не одинаковы, то все просто: запустить счетчик +- и если счетчик 0 то это и есть медиана.
        # для равных элементов пришлось повозиться и дополнительно почитать теорию.
        # суть не в просто больше или меньше, а именно не меньше и не больше
        if less <= len(some_arr) / 2 and (less + equal) >= len(some_arr) / 2 + 1:
            return some_arr[i]


if __name__ == '__main__':
    def median_by_sort(some_arr):
        some_arr.sort()
        result = some_data[len(some_data) // 2]
        return result


    def median_by_marge(some_arr):
        PE_les_7_task_2.my_marge_sort(some_arr)
        result = some_data[len(some_data) // 2]
        return result


    MAX_RANGE = 50
    MIN_RANGE = 0
    SIZE = 2 * int(input('Введите натуральное число для формирования массива: ')) + 1

    some_data = [randint(MIN_RANGE, MAX_RANGE) for x in range(SIZE)]  # без вещественных для удобства
    print('Дано:', '\n', some_data)
    print('-' * 45)
    print('Результат без сортировки:', '\n', my_median(some_data))
    print('Время на 1000 попыток: ', '\n', timeit(f'my_median({some_data})', number=1000, globals=globals()))
    print('-' * 45)
    print('Контроль встроенной сортировкой:', '\n', median_by_sort(some_data))
    print('Время на 1000 попыток: ', '\n', timeit(f'median_by_sort({some_data})', number=1000, globals=globals()))
    print('-' * 45)
    print('Контроль слиянием:', '\n', median_by_marge(some_data))
    print('Время на 1000 попыток: ', '\n', timeit(f'median_by_marge({some_data})', number=1000, globals=globals()))
