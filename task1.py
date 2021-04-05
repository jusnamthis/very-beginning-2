# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя
# пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл
# в данном случае использовать функцию re.compile()?


import re

RE_PARSE = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)')


def email_parse(email_address):
    parsed_email = RE_PARSE.match(email_address)
    if parsed_email:
        return parsed_email.groupdict()
    else:
        raise ValueError('Something went wrong')


print(email_parse('someone@geekbrains.ru'))


# Думаю, что в данном случае нет необходимости использовать re.compile, т.к обрабатываем очень малое количество инф-ии
# Если была бы необходимость в использовании данной регулярки или имели бы дело с обработкой большого количества инф-ии,
# Тогда re.compile() было бы уже оправдано. Я написал, чтобы больше вникнуть в тему
