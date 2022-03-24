# Задание 4
# Определить, какое число в массиве встречается чаще всего.

# постановка задачи
import random

SIZE = 20
RANGE_MIN = 0
RANGE_MAX = 10

array_ = [random.randint(RANGE_MIN, RANGE_MAX) for _ in range(SIZE)]
print('Дано')
print(array_)
print('-' * 45)

# решение
print('Решение за 1 проход массива. Дополнительный словарь и множество. !!!Первый максимум!!!')

result_dict = {}
spam_set = set()
max_numb = array_[0]
max_frq = 1

for el in array_:  # один проход по массиву
    if el in spam_set:  # говорят что быстро работает :). можно через setdefault
        result_dict[el] = result_dict.get(el) + 1  # подкручиваем счетчик по нужным ключам
    else:
        spam_set.add(el)
        result_dict[el] = 1
    if result_dict.get(el) > max_frq:  # сравнили налету и переписали результат если нужно.
        max_numb, max_frq = el, result_dict.get(el)

if max_frq == 1:
    print('Все значения уникальны')
else:
    print(f'Значение "{max_numb}" встречается {max_frq} раз(а)')

# ---------------------------------------------------------------------------------
print('-' * 45)

print('Вариант с меньшими затратами памяти, но не времени. ...наверное. !!!Первое значение из макс.!!!')

max_frq = 1
for el in array_:
    frq = 0
    for i in array_:
        if i == el:
            frq += 1
    if frq > max_frq:  # !!!по первому значению имеющему максимальную частоту!!!
        max_frq = frq
        max_numb = el

if max_frq == 1:
    print('Все значения уникальны')
else:
    print(f'Значение "{max_numb}" встречается {max_frq} раз(а)')
