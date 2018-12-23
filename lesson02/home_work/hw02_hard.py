__author__ = 'Melchuk Andrey'
import datetime

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
print("\n\ntask1")

if equation.find('='):
    split_eq = equation.split('=')
    print(split_eq)

    if split_eq[1].find('x'):
        split_x = split_eq[1].split('x')
        print(split_x)

        k = float(split_x[0].replace(' ', ''))
        print("k =", k)
        b = float(split_x[1].replace(' ', ''))
        print("b =", b)
        y = k * x + b

        print(y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date1 = '01.11.1985'

# Примеры некорректных дат
date2 = '01.22.1001'
date3 = '1.12.1001'
date4 = '-2.10.3001'

print("\n\ntask2")


def is_date_valid(date_ptr):
    split_date = date_ptr.split('.')
    print('\ndate =', split_date)

    if not (len(split_date[0]) == 2 and len(split_date[1]) == 2 and len(split_date[2]) == 4):
        print("Incorrect format.")
    else:

        day = int(split_date[0])
        month = int(split_date[1])
        year = int(split_date[2])

        if day < 1 or day > 31 or month < 1 or month > 12 or year < 0 or year > 9999:
            print("Incorrect date values")
        else:
            print("Correct date")


is_date_valid(date1)
is_date_valid(date2)
is_date_valid(date3)
is_date_valid(date4)

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


print("\n\ntask3")


def get_room(dest_room):
    print('\nEntrance = ', dest_room)
    count = 0
    stage = 0
    top_floor_of_stage = 0

    while (count < dest_room):
        stage += 1
        count += stage * stage
        top_floor_of_stage += stage
    # print('counted =', count, 'stage =', stage, 'top_floor =', top_floor_of_stage)

    in_stage_count = stage * stage - (count - dest_room)
    # print('in_stage_count', in_stage_count)

    in_stage_floor = (in_stage_count - 1) // stage + 1
    # print('in_stage_floor', in_stage_floor)

    dest_floor = stage + in_stage_floor
    print('Exit::floor = ', dest_floor)

    dest_exit = stage - (in_stage_floor * stage - in_stage_count)
    print('Exit::door', dest_exit)


get_room(11)
get_room(13)
