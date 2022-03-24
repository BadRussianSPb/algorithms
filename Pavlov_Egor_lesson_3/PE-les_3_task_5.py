# Задание 5
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 20
RANGE_MIN = -10
RANGE_MAX = 10

array_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(SIZE)]
print('Дано')
print(array_)
print('-' * 45)

# решение
print('Решение. Позиция по первому вхождению.')

min_numb = 0
numb_idx = 0
for i, el in enumerate(array_):
    if el < 0:
        if min_numb != 0:
            if abs(el) < abs(min_numb):  # <= даст последнее вхождение искомого элемента
                numb_inx, min_numb = i, el
        else:
            numb_idx, min_numb = i, el
if min_numb == 0:
    print('Элементы удовлетворяющие условию не найдены')
else:
    print(f'Максимальным отрицательным элементом является: {min_numb}. Его позиция: {numb_idx}')
