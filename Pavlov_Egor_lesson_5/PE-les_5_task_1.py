# Задание 1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple


def new_comp(count):
    """
    Функция создает данные для инициализации новой записи в именованном кортеже.
    """
    name_of_comp = input(f'Введите название предприятия {count + 1}: ')
    quarters = [float(_) for _ in input(f'Введите показатели "{name_of_comp}" за 4 квартала через пробел: ').split()]
    year = sum(quarters)
    return name_of_comp, *quarters, year


Company = namedtuple('Company', 'name quarter_1 quarter_2 quarter_3 quarter_4 in_year')
vol_of_comp = int(input('Введите количество предприятий: '))
company = [0 for _ in range(vol_of_comp)]  # список для всех компаний
all_in_year = 0  # начинаем считать среднюю
more_then_avr = []  # пытался решить быстрой сортировкой и потом разбить пополам, но с именоваными кортежами не осилил
less_then_avr = []
just_avr = []

for i in range(vol_of_comp):
    company[i] = Company._make(new_comp(i))  # дабавляем в список новую запись из именованного кортежа
    all_in_year += getattr(company[i], 'in_year') / vol_of_comp  # продолжаем накапливать среднюю

for comp in company:
    name, in_year = getattr(comp, 'name'), getattr(comp, 'in_year')
    if in_year > all_in_year:
        more_then_avr.append([name, in_year])
    elif in_year < all_in_year:
        less_then_avr.append([name, in_year])
    else:
        just_avr.append([name, in_year])  # и такой вариант может быть как с 1 там и несколькими предприятиями

print('-' * 45)
print(f'Средняя прибыль за год составляет: {all_in_year}')
print('-' * 45)
print(f'Предприятия и их прибыль меньше средней:')
print(*less_then_avr, sep='\n')
print('-' * 45)
print(f'Предприятия и их прибыль больше средней:')
print(*more_then_avr, sep='\n')
print('-' * 45)
print(f'Предприятия и их средняя прибыль:')
print(*just_avr, sep='\n')
