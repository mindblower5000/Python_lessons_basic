
__author__ = 'Melchuk Andrey'
import random

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
print("\ntask 1")
src_value = int(random.random() * 10000)
print("value = ", src_value)

while src_value > 0:
    r = int(src_value % 10)
    print(r)
    src_value = (src_value - r) / 10



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
print("\ntask 2")


a = 4
b = 5

print("a = ", a, ", b = ", b)
a += b
b = a - b
a -= b

print("a = ", a, ", b = ", b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
print("\ntask 3")

if int(input("Enter your age:")) < 18:
    print("Извините, пользование данным ресурсом только с 18 лет")
else:
    print("Доступ разрешен")
