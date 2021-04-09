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


class Clothes(ABC):

    @property
    def cloth_size(self):
        return self.get_size()

    @abstractmethod
    def get_size(self):
        print('Я вычисляю количество ткани')


class Suit(Clothes):
    fabric_size = 0

    @property
    def cloth_size(self):
        return self.get_size()

    def __init__(self, height):
        self.height = height

    def get_size(self):
        return 2 * self.height + 0.3


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def cloth_size(self):
        return self.get_size()

    def get_size(self):
        return self.size * 6.5 + 0.5


coat = Coat(3)
print(coat.cloth_size)

suit = Suit(15)
print(suit.cloth_size)
