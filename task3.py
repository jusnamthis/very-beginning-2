# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно,
# что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями —
# запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения —
# данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби,
# меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ. Фрагмент файла с данными о
# пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи

import json

with open('users.csv', 'r', encoding='utf8') as f:
    users_names = f.read()
    names = users_names.splitlines()

with open('hobby.csv', 'r', encoding='utf8') as f:
    users_hobbies = f.read()
    hobbies = users_hobbies.splitlines()

result = {}
for i in range(0, len(names)):
    if len(names) < len(hobbies):
        exit(1)
    elif i < len(hobbies):
        result[names[i].replace(',', ' ')] = hobbies[i]
    else:
        result[names[i].replace(',', ' ')] = None

with open('names_and_hobbies.json', 'w', encoding='utf8') as f:
    json.dump(result, f)

