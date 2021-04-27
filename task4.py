# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте
# параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
# постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class WareHouse:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = {}
        self.movements = {}

    def to_take(self, device, amount):
        if amount > self.capacity:
            raise ValueError('Склад не может вместить такое кол-во оборудования!') #6
        if self.storage.get(device) is None:
            self.storage.setdefault(device, amount)
        else:
            prev_value = self.storage.get(device)
            self.storage[device] = prev_value + amount

    def remove(self, device, amount):
        try:
            if self.storage.get(device) is None:
                raise ValueError('Товаров такого типа нет на складе!') #6
        except ValueError as err:
            print(err)
        else:
            prev_value = self.storage.get(device)
            self.storage[device] = prev_value - amount

    def move(self, device, department, amount):
        self.remove(device, amount)
        self.movements.setdefault(department, {})
        prev_value = self.movements[department].get(device) if self.movements[department].get(device) != None else 0
        self.movements[department].setdefault(device, prev_value + amount)


class OfficeEquip:
    def __init__(self, name, occupied_space):
        self.name = name
        self.space = occupied_space


class Printer(OfficeEquip):
    def __init__(self, name, occupied_space, paper_type):
        if isinstance(occupied_space, (int, float)) is False:
            raise ValueError('Количество занимаемого места должно быть числом, а не строкой!')
        super().__init__(name, occupied_space)
        self.paper_type = paper_type


class Scaner(OfficeEquip):
    def __init__(self, name, occupied_space, paper_size):
        super().__init__(name, occupied_space)
        self.paper_size = paper_size


class Xerox(OfficeEquip):
    def __init__(self, name, occupied_space, color):
        super().__init__(name, occupied_space)
        self.color = color


p_1 = Printer('hp', 3, 'A3')
s_1 = Scaner('Asus', '2', '230*160')
x_1 = Xerox('Xerox', '6', 'colored')

warehouse = WareHouse(40)
warehouse.to_take(p_1, 24)
print(warehouse.storage)
warehouse.remove(p_1, 22)
print(warehouse.storage)
warehouse.move(p_1, 'Financial', 15)
print(warehouse.movements)
