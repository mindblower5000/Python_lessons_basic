# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print('\n\ntask 1')


def fibonacci(n, m):
    def fib(num):
        if num < 2:
            return num
        return fib(num - 1) + fib(num - 2)

    for i in range(n, m + 1):
        print(i, fib(i))


fibonacci(0,20)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print('\n\ntask 2')


def sort_to_max(origin_list):
    new_list = list(origin_list)
    quick_sort(new_list, 0, len(new_list) - 1)
    return new_list


def quick_sort(nums, left, right):
    if left >= right:
        return
    i, j = left, right
    center_val = nums[(left + right) // 2]

    while i <= j:
        while nums[i] < center_val:
            i += 1
        while nums[j] > center_val:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quick_sort(nums, left, j)
    quick_sort(nums, i, right)


l = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(l)
print(sort_to_max(l))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print('\n\ntask 3')


def my_filter(function, src_list):
    result = []
    for elem in src_list:
        if function(elem):
            result.append(elem)
    return result


print(my_filter(lambda x: x > 0, [100, 3, -4, 10, -20]))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print('\n\ntask 4')

#  1 2 3 4 5
# 1  *****
# 2  *   *
# 3  *   *
# 4  *****
# 5


def check_points(x1, y1, x2, y2, x3, y3, x4, y4):
    if y1 - y4 and y2 - y3 and x2 - x1 == x3 - x4:
        print('Точки являются вершинами параллелограмма')
    else:
        print('Точки не являются вершинами параллелограмма')


check_points(2,1, 4,1, 4,4, 2,4)
check_points(2,1, 4,1, 4,4, 1,4)


