# Задание 8
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

MAX_COLUMN = 4
MAX_STR = 5

result_list = []
sum_el = 0
for j in range(MAX_STR):
    result_list.append([])
    for i in range(MAX_COLUMN - 1):
        el = int(input(f'Введите {i + 1} элемент {j + 1} строки: '))
        result_list[j].append(el)
        sum_el += el
    result_list[j].append(sum_el)
    sum_el = 0

print('Итоговая матрица 5х4')
for el in result_list:
    for i in el:
        print(f'{i:>5}',  end='')
    print()
