# Задание 1
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# постановка задачи

DIV_MIN = 2
DIV_MAX = 9
RANGE_MIN = 2
RANGE_MAX = 99

# решения

print('Вариант с целым от деления.')

for i in range(DIV_MIN, DIV_MAX + 1):
    print(f'Для делителя "{i}" подходящих значений: {RANGE_MAX // i}')

# ---------------------------------------------------------------------------------
print('-' * 45)

print('Вариант с шагом. Если вдруг есть массив со значениями не подряд.')

for i in range(DIV_MIN, DIV_MAX + 1):
    result = 0
    for j in range(RANGE_MIN, RANGE_MAX + 1, i):
        result += 1
    print(f'Для делителя "{i}" подходящих значений: {result}')

# ---------------------------------------------------------------------------------
print('-' * 45)

print('Вариант "топорный" первый пришедший в голову с перебором и проверкой всех значений ряда.')

start = RANGE_MIN

for i in range(DIV_MIN, DIV_MAX + 1):
    result = 0
    for j in range(start, RANGE_MAX + 1):
        if j % i == 0:
            result += 1
    print(f'Для делителя "{i}" подходящих значений: {result}')
    start += 1  # 3 для 2 или 4 для 2 и 3 в любом случае не делитель
