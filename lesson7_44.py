"""
4.	Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках),
размер которых не превышает этой границы, но больше предыдущей (начинаем с 0),
"""

from os import stat, scandir, walk
from os.path import join, isfile, basename, abspath
import json

input_folder = '1'  # каталог где будет проводиться сканирование
folder = join(".", input_folder)

folder_files = []
for root, dirs, files in walk(folder):  # проходимя по каталогу и подпапкам
    for item in scandir(root):
        if isfile(item):
            folder_files.append(item)
max_f_size = (max(map(lambda x: x.stat().st_size, folder_files)))  # определяем размер файлв

stat_folder = dict()
i = 100
while i <= max_f_size*10:  # сортируем файлы по размеру и склеиваем в словарь
    stat_folder[i] = [len([f for f in folder_files if i/10 < f.stat().st_size <= i]), list(set(str(f).split(".")[-1][:-2] for f in folder_files if i/10 < f.stat().st_size <= i))]
    i *= 10
stat_folder[100][0] += (len([v for v in folder_files if v.stat().st_size <= 10]))
stat_folder[100][1].extend(list(set(str(f).split(".")[-1][:-2] for f in folder_files if f.stat().st_size <= 10)))
print(stat_folder)

with open(join(folder, "stat_folder.json"), "w", encoding="UTF-8") as file:
    json.dump(stat_folder, file)
