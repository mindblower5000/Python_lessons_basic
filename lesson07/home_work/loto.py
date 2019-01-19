#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random




class BarrelsGenerator:
    """
    BarrelsGenerator - my random.choice iterator
    """
    def __init__(self, size):
        self.size = size
        self.sorted_list = []
        self.random_list = []  # final container
        self.map_iter = None  # final iterator
        self.reset()

    """
    Reset iterator to new generated random order for the list from 1 to size
    """
    def reset(self):
        for index in range(1, self.size + 1):
            self.sorted_list.append(index)
        sorted_len = len(self.sorted_list)
        while sorted_len > 0:
            sorted_len = len(self.sorted_list)
            if sorted_len > 0:
                random_index = random.randint(0, sorted_len - 1)
                self.random_list.append(self.sorted_list[random_index])
                self.sorted_list.remove(self.sorted_list[random_index])
        self.map_iter = map(int, self.random_list)

    def __next__(self):
        return next(self.map_iter)

    def __iter__(self):
        return self.map_iter

    @property
    def list(self):
        return self.random_list


class Card90:
    def __init__(self, user, card_header):
        self.user = user
        self.card_header = card_header
        self.barrel_generator = BarrelsGenerator(90)
        self.card_line1 = self.barrel_generator.list[0:5]
        self.card_line2 = self.barrel_generator.list[10:15]
        self.card_line3 = self.barrel_generator.list[20:25]
        self.card_line1.sort()
        self.card_line2.sort()
        self.card_line3.sort()
        #  mark random spaces as -1
        for i in range(0, 4):
            self.card_line1.insert(random.randint(0, 4 + i), -1)
        for i in range(0, 4):
            self.card_line2.insert(random.randint(0, 4 + i), -1)
        for i in range(0, 4):
            self.card_line3.insert(random.randint(0, 4 + i), -1)

    def __str__(self):
        msg = ('{}\n'.format(self.card_header))
        for x in self.card_line1:
            msg += '{: <2} '.format(x if x > 0 else ('' if x == -1 else '-'))
        msg += '\n'
        for x in self.card_line2:
            msg += '{: <2} '.format(x if x > 0 else ('' if x == -1 else '-'))
        msg += '\n'
        for x in self.card_line3:
            msg += '{: <2} '.format(x if x > 0 else ('' if x == -1 else '-'))
        msg += '\n--------------------------'
        return msg

    def check(self, barrel):
        for i1, x1 in enumerate(self.card_line1):
            if x1 == barrel:
                return 1, i1, x1
            else:
                for i2, x2 in enumerate(self.card_line2):
                    if x2 == barrel:
                        return 2, i2, x2
                    else:
                        for i3, x3 in enumerate(self.card_line3):
                            if x3 == barrel:
                                return 3, i3, x3

        return None, None, None

    """
    If all numbers have been striked returns true
    """

    def is_empty(self):
        stat = True if sum(self.card_line1) == -14 and sum(self.card_line2) == -14 and sum(
            self.card_line3) == -14 else False
        if stat:
            print(self.user)
            print(self.card_line1)
            print(self.card_line2)
            print(self.card_line3)
        return stat

    """
    Strike number by  dest_line and dest index, set value to -2
    """

    def strike_number(self, dest_line, j, x):
        if dest_line == 1 and self.card_line1[j] == x:
            self.card_line1[j] = -2
            return True
        if dest_line == 2 and self.card_line2[j] == x:
            self.card_line2[j] = -2
            return True
        if dest_line == 3 and self.card_line3[j] == x:
            self.card_line3[j] = -2
            return True
        print('strike_number:: strike error. {} {} {}'.format(dest_line, j, x))
        return False


barrels_container = BarrelsGenerator(90)
user_card = Card90('Пользователь', '------ Ваша карточка -----')
pc_card = Card90('Компьютер', '--- Карточка компьютера --')


def play(card: Card90, barrel):
    barrel_is_at_line, card_j, card_value = card.check(barrel)
    if barrel_is_at_line is not None:
        # print('!! Strike {} at line {}, position {}'.format(card_value, barrel_is_at_line, card_j))
        if card.strike_number(barrel_is_at_line, card_j, card_value):
            if user_card.is_empty():
                print('{} выиграл. Стоп игра.'.format(card.user))
                return 2  # Winner
            else:
                print('{} зачеркнул число {}.'.format(card.user, barrel))
                return 1  # Strike
    return 0  # Missed


player = True  # True - user, False - pc
cards = [pc_card, user_card]
computer_answers = ['y', 'n']
# MAIN
for i, b in enumerate(barrels_container):

    print('\nХод {}. Ходит {}. Новый бочонок: {} (осталось {})'.format(i, cards[int(player)].user, b, 90 - i - 1))
    print(cards[0])
    print(cards[1])

    luck = -1
    q = None
    if player:
        q = input('Зачеркнуть цифру? (y/n/q)')
    else:
        #  q = random.choice(computer_answers)  # stupid computer mode
        if cards[int(player)].check(b)[0] is not None:  # smart computer mode
            q = 'y'
        else:
            q = 'n'

    if q == 'q' or q == 'й':
        print('Игра остановлена пользователем!')
        break
    if q == 'y' or q == 'н':
        print('Выбрано - Зачеркиваем цифру:')
        luck = play(cards[int(player)], b)
        if luck == 1:
            print('Удачно! Игра продолжается.')
            player = not player  # из правил непонятно основание для перехода хода или все проверяют поочереди...?????
            continue
        elif luck == 2:
            print('Ура! Победа! {}'.format(cards[int(player)].user))
            break
        elif luck == 0:
            player = not player
            print('Не верно! Число то есть! {} проиграл!'.format(cards[int(player)].user))
            break
    elif q =='n' or q == 'т':
        print('Выбрано - Продолжить:')
        if cards[int(player)].check(b)[0] is not None:   # number found
            player = not player
            print('Не верно! Цифра есть! {} проиграл!'.format(cards[int(player)].user))
        else:
            print('Верно! Цифры нет! продолжаем')
            player = not player


print('Игра окончена.')
print(cards[0])
print(cards[1])