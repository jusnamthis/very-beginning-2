from requests import get, utils
import datetime
from decimal import Decimal


def get_currency_rate(content, currency):
    currency = currency.upper()
    string = '' # избавляюсь от "<>" для того, чтобы можно в последствии была возможность пользоваться словами в тегах, например value или valute
    for letter in content:
        if letter not in ('<', '>'):
            string += letter
        else:
            string += ' '

    content_list = list(string.split()) # преобразую полученную строку в список, перед этим сделав сплит, что позволило работать со словами в тегах, например valute

    the_date = []
    for element in content_list:
        if 'Date' in element:
            date_ls = element.split('"')
            un_date = date_ls[1].split('.')
            the_day = int(un_date[0])
            the_month = int(un_date[1])
            the_year = int(un_date[2])
            the_date = datetime.date(year=the_year, month=the_month, day=the_day)


    for i in range(0, len(content_list)):
        if content_list[i] == 'Valute':
            start = i
        if content_list[i] == '/Valute':
            finish = i
            foo = lookin_for_price(content_list[start + 1:finish], currency) # проверяю является ли валюта необходимой пользователю, проверяя значения для каждой валюты, завёрнутые в теги valute
            if isinstance(foo, float):
                return Decimal(foo), the_date
    return None


def lookin_for_price(some_list, user_cur): # получает срез, в котором находятся значения каждой валюты, постепенно перебирая все валюты - мы находим необходимуб
    for element in some_list:
        if element == user_cur:
            print(f'{user_cur} = {some_list[-2]} рублей')
            return to_dot(some_list[-2])


def to_dot(string_num): # избавляется от запятой, для последующего преобразования в число с плав. точкой
    res = ''
    for symbol in string_num:
        if symbol == ',':
            res += '.'
        else:
            res += symbol
    return float(res)


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)
print(get_currency_rate(content, 'USD'))
get_currency_rate(content, 'EUR')
