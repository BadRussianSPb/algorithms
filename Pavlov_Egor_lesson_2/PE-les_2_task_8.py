# Задание 8
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

def building_string(k, spam=''):
    if k > 0:
        spam += input(f'Введите число (осталось {k}): ')
        return building_string(k - 1, spam)
    else:
        return spam


k = int(input('Введите кол-во чисел: '))
x = input('Введите цифру для поиска: ')
result = 0
for el in building_string(k):
    if el == x:
        result += 1

print(f'Количество совпадений для числа "{x}": {result}')
