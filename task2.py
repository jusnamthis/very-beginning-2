# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
#
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
#
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не
# программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os


def parse_line(string):
    dash_pos = 0
    stick_chr = string[0]
    while stick_chr != '-':
        dash_pos += 1
        stick_chr = string[dash_pos]
    return dash_pos - 1 # поиск первого тире


current_directory = os.path.abspath(os.path.curdir) # эта переменная отвечает за директорию, в которой я нахожусь в
# данный момент, она используется для того, чтобы подниматься по каталогу или углубляться в него
print(current_directory)
previous_pos = 0 # переменная служащая для сохранения иерархии: если предыдущая строчка содержала в себе больше
# пробелов - следовательно она ниже по иерархии и наоборот
with open('config.yaml', 'r', encoding='utf8') as f:
    for line in f:
        new_pos = parse_line(line) # здесь я получаю количество пробелов в строке, так сравнивая предыдущее
        # количество и нынешнее - я могу понять; подниматься мне или опускаться по иерархии
        if new_pos >= previous_pos:
            if '.' in line: # по наличию точки в строке - я понимаю файл это или папка, если есть точка - значит за
                # ней следует расширение, а значит это файл и углубляться по иерархии не нужно, достаточно лишь создать
                with open(f'{current_directory}/{line[new_pos+3:].strip()}', 'w') as faa:
                    print(f'{current_directory}/{line[new_pos+3:].strip()}file was create')
            else: # если это папка, то я создаю её и углубляюсь
                os.mkdir(os.path.join(current_directory, line[new_pos+3:].strip()))
                current_directory = os.path.join(current_directory, line[new_pos+3:].strip())
        else:
            difference = (previous_pos - new_pos) // 3 # если старое количество пробелов больше, чем новое, значит
            # надо вверх, тут я вычисляю насколько позиций вверх нужно подняться
            for _ in range(difference):
                current_directory = os.path.join(current_directory, '..')
                print(os.path.abspath(current_directory)) # поднявшись - я создаю файл или папку
            if '.' in line:
                with open(f'{current_directory}/{line[new_pos+3:].strip()}', 'w') as faa:
                    print(f'{current_directory}/{line[new_pos+3:].strip()}file was create')
            else:
                os.mkdir(os.path.join(current_directory, line[new_pos+3:].strip()))
                current_directory = os.path.join(current_directory, line[new_pos+3:].strip())
        previous_pos = new_pos # присваиваю значение для сравнения