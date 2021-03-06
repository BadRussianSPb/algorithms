# -----------------------------------------------------------------------------------
# Задание №3
# По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y = kx + b, проходящей через эти точки.
# -----------------------------------------------------------------------------------

x1, y1 = int(input('Введите точку x1: ')),  int(input('Введите точку y1: '))
x2, y2 = int(input('Введите точку x2: ')),  int(input('Введите точку y2: '))
if x1 == x2:
    print(f"Составить каноническое уравнение нельзя. Прямая параллельна OY и имеет вид x = {x1}")
else:

    k = (y1 - y2) / (x1 - x2)
    b = y1 - (k * x1)
    if b < 0:
        print(f'Уравнение прямой имеет вид: y={k}x{b}')
    else:
        if b == 0:
            print(f'Уравнение прямой имеет вид: y={k}x')
        else:
            print(f'Уравнение прямой имеет вид: y={k}x+{b}')
