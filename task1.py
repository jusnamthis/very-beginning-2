# 1. Создать класс TrafficLight (светофор).
#
#     определить у него один приватный атрибут color (цвет) и метод get_current_signal() (получить текущий цвет);
#     после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью: красный (3 сек), жёлтый (1 сек), зелёный (3 сек);
#     переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
#     проверить переключение режимов работы светофора, опрашивая в цикле текущее состояние светофора с интервалом 0.5 секунды, используя метод get_current_signal().

from time import sleep


class TrafficLight:
    __color = 'Color'

    def get_current_signal(self):
        color = 'Red'
        print(color)
        sleep(3)
        color = 'Yellow'
        print(color)
        sleep(1)
        color = 'Green'
        print(color)
        sleep(3)


a = TrafficLight()
while True:
    sleep(0.5)
    a.get_current_signal()

# В целом код вышел рабочий, но не совсем понравилась реализация, думал что можно запихнуть в декоратор идея была
# следующая: создать экземпляр, обернуть инит в декоратор, который меняет цвета (change_signal_colors) а затем
# возвращает get current signal, но из-за того, что мы передаём ещё и self в качестве параметра - сбилось понимание
# того, как это сделать, и возник вопрос: есть ли в этом необходимость, возможно красота бы обернулась путаницей


# def __init__(self, func):
#
#     def change_signal_color(*args, **kwargs):
#         for color in args:
#             print(color)
#             sleep(1)
#         return func(*args, **kwargs)
#
#     return change_signal_color
#
# @__init__
# def get_current_signal(self, 'Red', 'Yellow', 'green'):
#     color = 'Red'
#     sleep(3)
#     color = 'Yellow'
#     sleep(1)
#     color = 'Green'
#     sleep(3)
