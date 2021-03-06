
__author__ = 'Melchuk Andrey'

import datetime
import random


# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
print("\n\ntask1")
l1 = [2, -5, 8, 9, -25, 25, 4]
l2 = []

print(l1)
l2 = [int(elem**.5) for elem in l1 if elem >= 0 and (elem ** .5).is_integer()]
print(l2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print("\n\ntask2")

date_time_str = '02.11.2013'
date = datetime.datetime.strptime(date_time_str, '%d.%m.%Y')
print(date)


months = ["", "января", "Февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября",
          "ноября", "декабря"]
date01_31 = ["", "первое", "второе", "третье", "четвертое", "пятое", "шетое", "седьмое", "восьмое", "девятое", "десятое",
             "одинадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое", "шестнадцатое", "семнадцатое",
             "восемнадцатое", "девятнадцатое", "двадцатое", "двадцать первое", "двадцать второе", "двадцать третье",
             "двадцать четвертое", "двадцать пятое", "двадцать шестое", "двадцать седьмое", "двадцать восьмое",
             "двадцать девятое", "тридцатое", "тридцать первое"]

month = date.month
year = date.year
day = date.day

print(date01_31[day], months[month], year, "года")


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
print("\n\ntask3")
random_list = []
n = 20

for i in range(n):
    random_list.append( random.randint(-100, 100))

print(random_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print("\n\ntask4")

lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = list(set(lst))
lst3 = [elem for elem in lst if lst.count(elem) == 1]

print(lst)
print(lst2)
print(lst3)
