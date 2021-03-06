# Задание 1
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об
# ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности
# деления на ноль, если он ввел его в качестве делителя.

def calc(a, b, c):
    a, b = float(a), float(b)
    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    else:
        result = a / b
    return result


c = None

while c != 0:
    print('Введите два числа и математичсекий знак. Для выхода введите 0 вместо знака')
    a, b, c = input(), input(), input()
    if c == '-' or c == '+' or c == '/' or c == '*':
        if b != '0' and c != '//':
            print(f'Ответ {calc(a, b, c)}')
        else:
            print(f'На {b} делить нельзя! Попробуй еще разок.')
            continue
    else:
        if c != '0':
            print('Введите корректный мат. символ')
            continue
        else:
            break

print('Расчеты окончены. Программа завершена')
