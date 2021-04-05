# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
#
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


import os
from os.path import relpath
from collections import defaultdict


def to_10(number):
    number_length = len(str(number))
    return 10 ** number_length


path_data = './some_data'
files_sizes = defaultdict(list)
for root, dirs, files in os.walk(path_data):
    for file in files:
        size = to_10(os.stat(os.path.join(path_data, file)).st_size)
        files_sizes[size].append(os.stat(os.path.join(path_data, file)).st_size)

for key, val in sorted(files_sizes.items()):
    print(f'{key}\t{len(val)}')
