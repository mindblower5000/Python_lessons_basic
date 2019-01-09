import lesson05.home_work.hw05_easy as easy
import os
import time

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

inp = ''
while not inp.__eq__('5'):
    # cmd list
    print('\nВведите команду:\n1. Перейти в папку\n2. Просмотреть содержимое текущей папки\
    \n3. Удалить папку\n4. Создать папку\n5. Выход')

    # dir list
    print('\n..', end='',sep='')
    print(*['\nDIR ' + item for item in easy.list_dir(easy.root)[0]], end='',sep='')
    print(*['\n    ' + item for item in easy.list_dir(easy.root)[1]], end='',sep='')

    # actions
    if inp.__eq__('1'):
        ask_dirname = input('\nВведите имя дирректории для перехода>')
        os.chdir(os.path.join(easy.root, ask_dirname))
        easy.root_refresh()
        inp = ''
        continue
    elif inp.__eq__('2'):
        pass  # auto show
    elif inp.__eq__('3'):
        ask_dirname = input('\nВведите имя дирректории для удаления>')
        easy.delete_dir(easy.root, ask_dirname)
        inp = ''
        time.sleep(1)
        continue
    elif inp.__eq__('4'):
        ask_dirname = input('\nВведите имя дирректории для удаления>')
        easy.make_dir(easy.root, ask_dirname)
        inp = ''
        time.sleep(1)
        continue

    # cmd prompt
    print('\n\n',easy.root, '>', end='', sep='')

    # keyboard selection
    inp = input()
