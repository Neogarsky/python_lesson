"""Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
    |--settings
    |--mainapp
    |--adminapp
    |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах
(добавлять детали)?
"""
# import os  делает проверку на существоавание
import os

fille_boss = ('my_project')
file_inside = ('settings', 'mainapp', 'adminapp', 'authapp')
for file in file_inside:
    os.makedirs(os.path.join(fille_boss, file), exist_ok=True)