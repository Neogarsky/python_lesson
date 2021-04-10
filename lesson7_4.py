"""4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10), а значения

— общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
{
100: 15,
1000: 3,
10000: 7,
100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat."""
from shutil import copy, SameFileError
from os import walk, mkdir
from os.path import join, exists

dir = r'.\my_project'
new_dir_path = join(dir, 'templates')
if not exists(new_dir_path):
    mkdir(new_dir_path)
for directory, dirs, files in walk(dir):
    for file in files:
        if ".txt" in file:
            file_path = join(new_dir_path, directory.split("\\")[0])
            if not exists(file_path):
                mkdir(file_path)
            try:
                copy(join(directory, file), file_path)
            except SameFileError:
                break
                
