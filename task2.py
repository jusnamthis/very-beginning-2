# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class ZeroDivErr(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(num_1, num_2):
    if num_2 == 0:
        raise ZeroDivErr('Неверный ввод!')
    return num_1 / num_2


while True:
    num_1 = int(input('делимое: (чтобы выйти введите "!")'))
    if num_1 == '!':
        print('До свидания!')
        break
    num_2 = int(input('делитель: '))
    try:
        print(division(num_1, num_2))
    except ZeroDivErr as err:
        print('На ноль делить нельзя', err)
    else:
        print('Двигаемся дальше')
