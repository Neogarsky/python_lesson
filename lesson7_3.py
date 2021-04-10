"""3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками»
в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
-------------------------------------------- основная структура------------------------------
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
расположены в родительских папках (они играют роль пространств имён); предусмотреть
возможные исключительные
ситуации; это реальная задача, которая решена, например, во фреймворке django."""

# в данной задаче структура задана в ручную

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