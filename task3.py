# 3. Реализовать базовый класс Employee (сотрудник).
#
# определить атрибуты: name (имя), surname (фамилия), которые должны передаваться при создании экземпляра Employee;
# создать класс Position (должность) с аттрибутами employee (сотрудник/Employee), position (должность/str),
# income (вознаграждение/dict) - атрибуты также задаются при создании экземпляра класса; последний атрибут должен
# быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
# "bonus": bonus}; в классе Position реализовать методы получения полного имени сотрудника get_full_name() и дохода с
# учётом премии get_total_income() (wage + bonus); проверить работу примера на реальных данных: создать экземпляры
# классов Employee, Position, вывести на экран имя сотрудника, его должность и вознаграждение сотрудника,
# используя методы класса Position.


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Position(Employee):
    def __init__(self, name, surname, position, **income):
        super().__init__(name, surname)
        self.position = position
        self._income = sum(map(lambda key: income[key], income.keys()))

    def get_full_name(self):
        print(f"Hello to u {self.position}! {self.name} {self.surname}")

    def get_total_income(self):
        print(f"{self._income} the salary is")


programer = {
    'wage': 40000,
    'bonus': 5000
}

journalist = {
    'wage': 30000,
    'bonus': 10000
}

ivan = Position('Ivan', 'Petrov', 'programmer', **programer)
ivan.get_full_name()
ivan.get_total_income()

petr = Position('Petr', 'Denisovich', 'journalist', **journalist)
petr.get_total_income()
petr.get_full_name()



# Сначала написал вот так:
# class Position:
#     def __init__(self, position, **income):
#         # super().__init__(name, surname)
#         self.position = position
#         self._income = sum(map(lambda key: income[key], income.keys()))
#
#     def get_full_name(self, person):
#         print(f"Hello to u {self.position} {person}")
#
#     def get_total_income(self):
#         print(f"{self._income} the salary is")
#
# some_man = Employee('Ivan', 'Denisov')
# the_salary = Position('programmer', **programer)
# the_salary.get_full_name(some_man)
# the_salary.get_total_income()

# Но на выводе получал вместо ожидаемого имени следующее: <__main__.Employee object at 0x7f17fc015fd0>
# Поэтому сделал через наследование