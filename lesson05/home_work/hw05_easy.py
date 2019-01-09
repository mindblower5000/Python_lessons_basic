import os
import sys
import shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_dir(root_path, my_path):
    try:
        os.mkdir(os.path.join(root_path, my_path))
    except OSError:
        print('Создать директорию', my_path, 'не удалось')
    else:
        print('Успешно создана директория', my_path)


def delete_dir(root_path, my_path):
    try:
        os.rmdir(os.path.join(root_path, my_path))
    except OSError:
        print('Удалить директорию', my_path, 'не удалось')
    else:
        print('Успешно удалена директория', my_path)


root = os.getcwd()

if __name__ == "__main__":
    print('\nTask 1')

    for i in range(1, 10):
        make_dir(root, 'dir_' + str(i))

    for i in range(1, 10):
        delete_dir(root, 'dir_' + str(i))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(path):
    dir_listing = []
    dir_files = []
    for dirpath, dirnames, filenames in os.walk(path):
        dir_listing.extend(dirnames)
        dir_files.extend(filenames)
        break  # stops in current dir
    return dir_listing, dir_files


if __name__ == "__main__":
    print('\nTask 2')
    print(list_dir(os.getcwd())[0])  # 0 - dirs, 1 - files


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def make_copy(file_path):
    filename = os.path.basename(file_path)
    dirname = os.path.dirname(file_path)
    file = filename.split('.')
    try:
        shutil.copyfile(file_path, os.path.join(dirname, file[0] + '_copy.' + file[1]))
    except OSError:
        print('Не удалось скопировать', file_path)
    else:
        print('Успешно скопирован', file_path)

if __name__ == "__main__":
    print('\nTask 3')
    make_copy(sys.argv[0])


def root_refresh():
    global root
    root = os.getcwd()

