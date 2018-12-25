__author__ = 'Melchuk Andrey'
import math

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print('\n\ntask 1')


def my_round(number, ndigits):
    return round(number, ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print('\n\ntask 2')


def lucky_ticket(ticket_number):
    """
    Solution 1 - 1 Pass
    :param ticket_number:
    :return: True - means lucky ticket
    """
    count = (math.floor(math.log10(ticket_number)) + 1)  # calculate digits in number
    ah_sum = al_sum = 0
    index = 1
    while ticket_number > 0:
        r = int(ticket_number % 10)
        if index <= count // 2:
            al_sum += r
        elif count % 2 and index == (count + 1) / 2:
            pass
        else:
            ah_sum += r
        ticket_number = (ticket_number - r) / 10
        index += 1
    return ah_sum == al_sum


def lucky_ticket2(ticket_number):
    """
    Solution 2 - Extracting ah, ah by math
    :param ticket_number:
    :return: True - means lucky ticket
    """

    def sum_digits(number):  # return sum of digits for number
        my_sum = 0
        while number > 0:
            r = int(number % 10)
            my_sum += r
            number = (number - r) / 10
        return my_sum

    count = (math.floor(math.log10(ticket_number)) + 1)
    devider = 10 ** (count // 2)
    al = ticket_number % devider
    ah = (ticket_number - al) // devider
    if count % 2:
        ah //= 10
    return sum_digits(ah) == sum_digits(al)


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(43671))


print(lucky_ticket2(123006))
print(lucky_ticket2(12321))
print(lucky_ticket2(436751))
print(lucky_ticket2(43671))
