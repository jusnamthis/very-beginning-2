# . Реализуйте базовый класс Car.
#
# при создании класса должны быть переданы атрибуты: color (str), name (str). реализовать в классе методы: go(speed),
# stop(), turn(direction), которые должны изменять состояние машины - для хранения этих свойств вам понадобятся
# дополнительные атрибуты - придумайте какие. добавьте метод is_police() - который возвращает True/False,
# в зависимости от того является ли этот автомобиль полицейским (см.дальше) Сделайте несколько производных классов:
# TownCar, SportCar, WorkCar, PoliceCar; Добавьте в базовый класс метод get_status(), который должен возвращать в
# виде строки название, цвет, текущую скорость автомобиля и направление движения (в случае если автомобиль едет),
# для полицейских автомобилей перед названием автомобиля должно идти слово POLICE; Для классов TownCar и WorkCar в
# методе get_status() рядом со значением скорости должна выводиться фраза "ПРЕВЫШЕНИЕ!", если скорость превышает 60 (
# TownCar) и 40 (WorkCar). Создайте по одному экземпляру каждого производного класса. В цикле из 10 итераций,
# для каждого автомобиля сделайте одно из случайных действий: go, stop, turn со случайными параметрами. После каждого
# действия показывайте статус автомобиля.

from random import choice, randint

class Car:
    current_speed = 0
    current_direction = 'don\'t move now'


    def __init__(self, color, name, police=0):
        self.color = color
        self.name = name
        self.police = police

    def go(self, speed):
        print(f'Previous speed: {self.current_speed} km/h')
        print(f'Raise the speed to {speed + self.current_speed} km/h')
        self.current_speed += speed

    def stop(self):
        print('Car has stopped')
        self.current_speed = 0

    def turn(self, direction):
        self.current_direction = direction
        print(f'Moving at {self.current_direction}')
        self.current_direction = direction

    def get_status(self):
        if self.is_police():
            print(
                f'POLICE {self.color} {self.name} current speed - {self.current_speed}, moving {self.current_direction}')
        elif self.current_speed > 0:
            print(f'{self.color} {self.name} current speed - {self.current_speed}, moving {self.current_direction}')
        else:
            print(f'{self.color} {self.name} the car doesn\'t move')

    def is_police(self):
        if self.police:
            return True


class TownCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def get_status(self):
        if self.is_police():
            print(
                f'POLICE {self.color} {self.name} current speed - {self.current_speed}, moving {self.current_direction}')
        elif self.current_speed > 0:
            print(f'{self.color} {self.name} current speed - {self.current_speed}, moving {self.current_direction}')
        elif self.current_speed > 0 and self.current_speed > 60:
            print(f'{self.color} {self.name} current speed - {self.current_speed} , moving {self.current_direction}')
        else:
            print(f'{self.color} {self.name} the car doesn\'t move')


class WorkCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def get_status(self):
        if self.is_police():
            print(
                f'POLICE {self.color} {self.name} current speed - {self.current_speed}, moving {self.current_direction}')
        elif self.current_speed > 0:
            print(f'{self.color} {self.name} current speed - {self.current_speed}, moving {self.current_direction}')
        elif self.current_speed > 0 and self.current_speed > 40:
            print(f'{self.color} {self.name} current speed - {self.current_speed} , moving {self.current_direction}')
        else:
            print(f'{self.color} {self.name} the car doesn\'t move')


class SportCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name)

    def get_status(self):
        if self.is_police():
            print(
                f'POLICE {self.color} {self.name} current speed - {self.current_speed}, moving {self.current_direction}')
        elif self.current_speed > 0:
            print(f'{self.color} {self.name} current speed - {self.current_speed}, moving {self.current_direction}')
        else:
            print(f'{self.color} {self.name} the car doesn\'t move')


class PoliceCar(Car):
    def __init__(self, color, name, police):
        super().__init__(color, name, police)

    def get_status(self):
        if self.is_police():
            print(
                f'POLICE {self.color} {self.name} current speed - {self.current_speed}, moving {self.current_direction}')
        elif self.current_speed > 0:
            print(f'{self.color} {self.name} current speed - {self.current_speed}, moving {self.current_direction}')
        else:
            print(f'{self.color} {self.name} the car doesn\'t move')


# car.get_status()
# car.go(90)
# car.turn('Right')
# car.go(180)
# car.turn('Left')
# car.stop()
# car.get_status()

towncar = Car('Black', 'Toyota')
workcar = WorkCar('Red', 'Dodge')
sportcar = SportCar('Purple', 'Audi')
policecar = PoliceCar('White', 'Skoda', 1)

direct_list = ['Right', 'Left', 'Straight']

for _ in range(10):
    towncar.get_status()
    towncar.go(randint(0, 150))
    sportcar.stop()
    sportcar.get_status()
    sportcar.turn(choice(direct_list))
    sportcar.go(randint(0, 250))
    sportcar.get_status()
    policecar.turn(choice(direct_list))
    policecar.get_status()
    workcar.go(randint(0, 80))
    policecar.get_status()
    workcar.turn(choice(direct_list))
    policecar.get_status()
    workcar.turn(choice(direct_list))
    policecar.get_status()
    workcar.stop()
