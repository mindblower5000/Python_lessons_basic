import re
# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
from functools import reduce

print("Task 1")
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку
# matrix_trans = [*zip(*matrix)]

# solution 1
matrix_trans = [*zip(*matrix)]
print(matrix_trans)

# # solution 2
matrix_trans2 = [list(i) for i in zip(*matrix)]
print(matrix_trans2)

# # solution 3
matrix_trans3 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix_trans3)



# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
print("\n\nTask 2")
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
number = number.replace('\n', '')
exp5 = r'(?=(\d{5}))'
print(number)
fives = re.findall(exp5, number)
print(fives)

multi_list = [reduce(lambda a, x: int(a) * int(x), five) for five in fives]
multi_index = multi_list.index(max(multi_list))
print(multi_list)

print('Maximal sequence', fives[multi_index], 'multiplication is', max(multi_list), 'found at offset', multi_index)
print('Src data check:', number[multi_index: multi_index + 5])



# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
print("\n\nTask 3")

#   0   1   2   3   4   5   6   7
# 0 1
# 1             3               8
# 2
# 3     2               7
# 4
# 5         4       5
# 6
# 7                         6


queen_threat_directions = [[1, 0],
                           [1, 1],
                           [0, 1],
                           [-1, 1],
                           [-1, 0],
                           [-1, -1],
                           [0, -1],
                           [1, -1]]

queen_position = [[0, 0], [1, 3], [3, 1], [2, 5], [4, 5], [6, 7], [5, 3], [7, 1]]

chess_map = []


def this_move_is_valid(xy):
    if -1 < xy[0] < 8 and -1 < xy[1] < 8:
        if chess_map[xy[1]][xy[0]] > 0:
            return 1  # figure found
        else:
            return 0   # OK
    else:
        return -1  # out of the map


def get_next_turn_index(turn):
    if turn < 0 or turn >= 7:
        return -1           # end
    else:
        return turn + 1     # next


def get_coords(current_xy, direction_id):
    next_xy = [current_xy[0] + queen_threat_directions[direction_id][0],
               current_xy[1] + queen_threat_directions[direction_id][1]]
    return next_xy


def recursive_check_threat(current_xy, direction_id):
    start = 0
    end = 8
    if not direction_id == -1:  # not root do only one direction_id
        start = direction_id
        end = direction_id + 1

    detected_stat = 0  # everything is okay
    for direction in range(start, end):
        new_coord = get_coords(current_xy, direction)
        if this_move_is_valid(new_coord) == 0:      # OK
            if recursive_check_threat(get_coords(current_xy, direction), direction) == 1:
                detected_stat = 1
        elif this_move_is_valid(new_coord) == 1:    # figure detected
            print('THREAT DETECTED FROM', chess_map[new_coord[1]][new_coord[0]], 'AT', new_coord)
            detected_stat = 1
        else:
            pass

    return detected_stat


def reset_matrix():
    global chess_map
    chess_map = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]


def print_map():
    for line in chess_map:
        print(line)
    print('')


def init_positions(coord_pairs):
    for i, queen_xy in enumerate(coord_pairs):
        chess_map[queen_xy[1]][queen_xy[0]] = i + 1


reset_matrix()
init_positions(queen_position)
print_map()
print('QUEEN POSITIONS', queen_position)

for i, queen in enumerate(queen_position):
    print('\n#', i + 1)
    if recursive_check_threat(queen, direction_id=-1) == 1:
        print('* YES')
    else:
        print('* NO')
