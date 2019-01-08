import os
import sys
import shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print('\nTask 1')


def make_dir(my_path):
    root = os.getcwd()
    # print("Текущая рабочая директория", path)

    try:
        os.mkdir(os.path.join(root, my_path))
    except OSError:
        print('Создать директорию', my_path, 'не удалось')
    else:
        print('Успешно создана директория', my_path)


def delete_dir(my_path):
    root = os.getcwd()
    # print("Текущая рабочая директория", path)

    try:
        os.rmdir(os.path.join(root, my_path))
    except OSError:
        print('Удалить директорию', my_path, 'не удалось')
    else:
        print('Успешно удалена директория', my_path)


for i in range(1, 10):
    make_dir('dir_' + str(i))

#  !!! uncomment to delete them

# for i in range(1, 10):
#     delete_dir('dir_' + str(i))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print('\nTask 2')

dir_listing = []
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    dir_listing.extend(dirnames)

print(dir_listing)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print('\nTask 3')
print(sys.argv[0])
filename = os.path.basename(sys.argv[0])
dirname = os.path.dirname(sys.argv[0])
file = filename.split('.')
shutil.copyfile(sys.argv[0], os.path.join(dirname,file[0]+'_copy.'+file[1]))
