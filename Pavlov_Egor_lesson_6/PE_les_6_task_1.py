# Задание 1 урок 6
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

from sys import getsizeof
from sys import _getframe
from sys import version
import platform
import random


def my_size(y):
    """Функция 'собирает' в список внутри другой функции значения переменных с помощью vars()
     и накапливает(!) объем занимаемый ими памяти"""
    result = 0
    if isinstance(y, int) or isinstance(y, float) or isinstance(y, str):  # or isinstance(y, decimal)
        result += getsizeof(y)  # намучился особенно со строками ↑ (они тоже итерируются)
    else:
        for elem in y:
            if hasattr(elem, 'items'):  # условие для словарей
                result += getsizeof(elem)  # замерили сам словарь
                for key, value in elem.items():
                    result += getsizeof(key) + my_size(value)  # ключ замерили, значение отправили дальше в функцию
            elif hasattr(elem, '__iter__'):  # условие для остальных итерируемых переменных
                result += getsizeof(elem)  # замерили список/множество/кортеж
                for el in elem:
                    result += my_size(el)  # отправляем элементы в ункцию для замера
            else:
                result += getsizeof(elem)  # замеряем остальные числа и строки т.к. они не итерируются
    return result


# ---------------------------------------------------------------------------------------------------------
# для решения взяты варианты задания 3 из 2-го урока
# # Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# # Например, если введено число 3486, надо вывести 6843.

def from_the_end_v1(data, spam=''):
    if data == 0:
        return int(spam)
    else:
        print(f'{my_size([x for x in vars().values()])} байт занимают переменные в {_getframe().f_code.co_name}')
        return from_the_end_v1(int(data) // 10, spam + str(data % 10))


def from_the_end_v2(data):
    data = str(data)[::-1]
    print(f'{my_size([x for x in vars().values()])} байт занимают переменные в {_getframe().f_code.co_name}')
    return int(data)


def from_the_end_v3(data):
    data, spam = str(data), ''
    for i in range(len(data)):
        spam += data[len(data) - i - 1]
    print(f'{my_size([x for x in vars().values()])} байт занимают переменные в {_getframe().f_code.co_name}')
    return int(spam)


# ---------------------------------------------------------------------------------------------------------
n = random.randint(100_000_000, 1_000_000_000)

from_the_end_v1(n)
from_the_end_v2(n)
from_the_end_v3(n)

print('-' * 45)
print(version)
print(platform.architecture())

"""
485 байт занимают переменные в from_the_end_v1
508 байт занимают переменные в from_the_end_v2
1044 байт занимают переменные в from_the_end_v3
---------------------------------------------
3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)]
('64bit', 'WindowsPE')
"""

# Вариант 1 с рекурсией оказался самый наименее затратный по памяти. каждая рекурсия добавляет 51 байт.
# Стэк если не ошибаюсь освобождается сразу после выходы из каждой итерации.
# Второй вариант строковый "перевертыш" тоже неплох, но очевидно, что способ [::-1] тоже перебирает элементы
# Третий способ с циклом (читай дополнительная переменная i) самый затратный. Да, меняются ссылки,
# а значения потом сборщикм удаляются. Но сборщик приходит ведь не сразу?
