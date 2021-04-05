# 4. Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw() (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер); в каждом классе переопределить
# метод draw(). Для каждого класса метод должен выводить уникальное сообщение; создать экземпляры каждого класса и
# положить их в список. Проитерироваться по этому списку и вызвать метод draw() для каждого элемента.

class Stationery:
    title = 'Something'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Рисуем ручкой')

class Pencil(Stationery):

    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):

    def draw(self):
        print("Риусем маркером")


objects_list = []
pen = Pen()
objects_list.append(pen)
pencil = Pencil()
objects_list.append(pencil)
handle = Handle()
objects_list.append(handle)

for _ in objects_list:
    _.draw()
