# -----------------------------------------------------------------------------------
# Задание №1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# -----------------------------------------------------------------------------------

print("Введите целое трехзначное число:")
a = int(input())

if a < 0:
    a = -a
b = a % 10 + (a // 10 % 10) + a // 100
c = (a % 10) * (a // 10 % 10) * (a // 100)

print(f'Сумма цифр числа: {b}')
print(f'Произведение цифр числа: {c}')
