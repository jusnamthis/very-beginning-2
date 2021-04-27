# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

from datetime import date


class Data:

    def __init__(self, user_date):
        self.user_date = user_date
        self.check_info(user_date)

    @classmethod
    def to_date_transform(cls, user_date):
        d = user_date.split('-')
        for i in range(len(d)):
            d[i] = int(d[i])
        return date(d[2], d[1], d[0])

    @staticmethod
    def check_info(user_date):
        d = user_date.split('-')
        for i in range(len(d)):
            d[i] = int(d[i])
        if d[1] in [1, 3, 5, 7, 8, 10, 12] and d[0] > 31:
            raise ValueError('Проверьте число')
        elif d[1] in [4, 6, 9, 11] and d[0] > 30:
            raise ValueError('Проверьте число')
        elif d[1] == 2 and d[0] > 29:
            raise ValueError('Проверьте число')
        elif d[1] not in range(1, 13):
            raise ValueError('Проверьте месяц')
        else:
            print('Всё круто!')


print(Data.to_date_transform('20-07-1998'))
c = Data('30-02-1998')
