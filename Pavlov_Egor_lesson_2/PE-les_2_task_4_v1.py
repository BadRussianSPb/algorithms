# Задание 4 вариант 1
# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

def sum_of_elements(k, result=0.0, spam=1.0):
    result += spam
    if k > 0:
        return sum_of_elements(k - 1, result, (spam / -2))
    else:
        return result


k = int(input('Введите количество итераций: '))
if k == 0:
    print(0)
else:
    print(sum_of_elements(k - 1))
