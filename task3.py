# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
#
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

import os
from shutil import copytree

def check_dir(name):
    with os.scandir(name) as nest_dir:
        for element in nest_dir:
            if os.path.isdir(element) and os.path.dirname(element).endswith('templates') == False:
                check_dir(element)
            elif os.path.isdir(element) and os.path.dirname(element).endswith('templates'):
                print(f'templates was found {element}')
                copytree(element, f'./my_project/templates/{element}')


current_directory = os.path.abspath(os.path.curdir)
# os.rmdir('./templates')
# os.mkdir('./templates')
with os.scandir('./my_project') as it:
    for item in it:
        if not os.path.isdir(item):
            continue
        check_dir(item)
