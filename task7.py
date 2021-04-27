# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (
# комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNum:
    def __init__(self, real_num, imag_unit):
        self.real_num = real_num
        self.imag_unit = imag_unit

    def __add__(self, other):
        return ComplexNum(self.real_num + other.real_num, self.imag_unit + other.imag_unit)

    def __mul__(self, other):
        return ComplexNum(self.real_num * other.real_num - self.imag_unit * other.imag_unit,
                          self.real_num * other.imag_unit + self.imag_unit * other.real_num)

    def __str__(self):
        return f'{self.real_num} + {self.imag_unit}i'


complex_num1 = ComplexNum(9, 1)
complex_num2 = ComplexNum(4, 2)
print(complex_num1)
complex_num3 = complex_num2 + complex_num1
print(complex_num3)
complex_num4 = complex_num2 * complex_num3
print(complex_num4)