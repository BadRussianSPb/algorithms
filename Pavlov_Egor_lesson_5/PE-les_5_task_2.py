# Задание 2
# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from itertools import zip_longest

TABLE = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
         '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F',
         'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def my_hex_sum(x, y, hex_sum=deque(''), spam=0, count=1):  # последний аргумент задел на решение умножения сложением
    """
    Функция возвращает результат сложения шестнадцатеричных чисел a и b.
    """
    x, y = x[::-1], y[::-1]  # как в школе, начинаем с едениц, потом десятки и т.д. :)
    for x, y in zip_longest(x, y, fillvalue='0'):  # O(n) вместо O(n**2) помоему получается
        spam = TABLE[x] + TABLE[y] + TABLE[str(spam)]  # сложили два знечения и прибавили то, что было в уме
        if spam >= 16:
            hex_sum.appendleft(TABLE[str(spam - 16)])  # записали остаток
            spam = 1  # "десяток" в уме держим
        else:
            hex_sum.appendleft(TABLE[str(spam)])
            spam = 0  # или не держим...
    if spam:
        hex_sum.appendleft(TABLE[str(spam)])
    return hex_sum


def my_hex_multi(x, y, hex_multi=deque('')):
    """
    Функция возвращает результат умножения шестнадцатеричных чисел a и b.
    """
    spam = deque([deque() for _ in range(len(y))])  # создали список произведений для поочередного сложения
    x, y = deque(x), deque(y)
    for i in range(len(spam)):
        m = TABLE[y.pop()]  # берем поочередно единицы, десятки и т.д.
        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * TABLE[x[j]])  # записываем число полученное от умножения в список произведений
        for _ in range(i):
            spam[i].append(0)
    transfer = 0

    # приступаем к сложению всего что наумножали
    for _ in range(len(spam[-1])):
        res = transfer
        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()
        if res > 16:
            hex_multi.appendleft(TABLE[str(res % 16)])  # аналогия с сложением только обратное действие умножению
            transfer = res // 16
        else:
            hex_multi.appendleft(TABLE[str(res)])
    if transfer:
        hex_multi.appendleft(TABLE[str(transfer)])
    return hex_multi


a_b = input('Введите 2 шестнадцатеричных числа через пробел: ').split()
print('-' * 45)
print(f'Даны шестнадцатеричные числа {a_b[0]} и {a_b[1]}.')
print('-' * 45)
print('Результат сложения ', a_b[0], ' и ', a_b[1], ': ', *my_hex_sum(*a_b), sep='')
print('Результат перемножения ', a_b[0], ' и ', a_b[1], ': ', *my_hex_multi(*a_b), sep='')
