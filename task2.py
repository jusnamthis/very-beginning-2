# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
#
# Создать абстрактный класс Clothes (одежда). Сделать в этом классе свойство cloth_size
# (используя декоратор @property) - размер ткани, необходимый для производства одежды.
# Это свойство должно вычислять размерт ткани, вызывая абстрактный метод self.get_size().
# Сделать два производных класса одежды: Suit (костюм) и Coat (Пальто).
# В конструктор Suit должен принимать параметр height (рост), а Coat - size (размер).
# Для определения расхода ткани по каждому типу одежды внутри метода get_size() использовать формулы:
#
# для пальто: (size/6.5 + 0.5)
# для костюма: (2*height + 0.3)
#
# Создать список из 10 единиц одежды случайно выбирая один из двух возможных типов со случайным параметром.
# Распечатать список одежды: размер требуемой ткани, тип и параметр. Рассчитать и вывести на экран общий объем ткани,
# необходимый для пошива всей одежды из этого списка, используя свойство cloth_size. Например:
#
# 30.3 - Suit (height: 15)
# 20 - Coat (size: 3)
# 13.5 - Coat (size: 2)
# 4.3 - Suit (seze: 2)
# ...
# Итого: 250.3


from abc import ABC, abstractmethod
from random import randint


class Clothes(ABC):

    fabric_size = 0

    @property
    def cloth_size(self):
        print(f'Итого: {self.fabric_size}')

    @abstractmethod
    def get_size(self):
        print('что-то делаю')


class Suit(Clothes):

    @property
    def cloth_size(self):
        self.get_size()

    def __init__(self, height):
        self.height = height

    def get_size(self):
        fabric_amount = 2 * self.height + 0.3
        Clothes.fabric_size += fabric_amount
        print(f'{fabric_amount} - Suit (height: {self.height})')


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def cloth_size(self):
        self.get_size()

    def get_size(self):
        fabric_amount = self.size * 6.5 + 0.5
        Clothes.fabric_size += fabric_amount
        print(f'{fabric_amount} - Coat (height: {self.size})')




coat = Coat(randint(0, 50))
coat.cloth_size
suit = Suit(randint(0, 20))
suit.cloth_size
coat1 = Coat(randint(0, 50))
coat1.cloth_size
suit1 = Suit(randint(0, 20))
suit1.cloth_size
print(f'Итого: {Clothes.fabric_size}')



# Не совсем понял, как реализовать метод cloth_size, точнее исходя из условия - он должен вызывать метод get_size
# Если get_size вычисляет каждый раз под конкретный случай необходимое количество ткани, то он либо каждый раз
# выводит строку вида 30.3 - Suit (height: 15), либо возвращает значение, которое мы затем выводим т.е не совсем
# понятно, как в таком случае cloth_size может в конечном счёте вывести итог, не вызывая при этом get_size чтобы
# вывод был именно вида Итого: 250.3
# Поэтому сделал вывод уже в мейне, обратившись к переменной класса
# пайчарм сильно ругается на мои строки кода с 74 по 81, объясните почему, пожалуйста