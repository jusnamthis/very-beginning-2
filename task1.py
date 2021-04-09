# 1. Реализовать класс Matrix (матрица).
#
# Конструктор класса __init__() должен принимать список списков чисел для задания превоначального состояния матрицы.
# Подсказка: матрица — это таблица размером N строк на M столбцов (размерность N x M).
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
#
# В методе __init__() надо проверить корректность передаваемых данных - все списки должны быть одинаковой длины. В
# случае расхождения выбрасывать исключение ValueError с соответствующим описанием. Добавить метод __add__() сложения
# двух матриц. Складывать можно матрицы одинаковой размерности. В случае, когда пользователь пытается сложить матрицы
# разных размеров выбросить исключение ValueError. В результате сложения двух матриц должна образоваться новая
# матрица размером N x M, где каждый элемент в ячейке i,j образован сложением значений из соответствующих ячеек
# исходных матриц. Реализовть метод __str__(), возвращающий строку вида " 1 2 3\n 4 5 6", отводя под числа по три
# разряда, чтобы для небольших чисел матрица выглядела как таблица. Создать три матрицы (две одинаковые по размеру и
# одну с другим размером). Сложить одинаковые матрицы и потом сложить разные. Напечатать исходные таблицы и результат
# сложения.


class Matrix:

    # def __init__(self, matrix_list):
    #     if len(matrix_list[0]) == len(matrix_list[1]):
    #         row_len = len(matrix_list[0][0])
    #         for j in range(len(matrix_list[0])):
    #             if row_len != len(matrix_list[0][j]) or row_len != len(matrix_list[1][j]):
    #                 raise ValueError('Проверьте введённые данные, длина рядов должна быть одинаковой')
    #     else:
    #         raise ValueError('Матрицы разные, проверьте ввод')
    #     print('Иницииализация прошла успешно')

    def __init__(self, matrix):
        self.matrix = matrix
        row_len = len(matrix[0])
        for _ in range(len(matrix)):
            if len(matrix[_]) != row_len:
                raise ValueError('Проверьте введённые данные, длина рядов должна быть одинаковой')
        print('Иницииализация прошла успешно')

    def __str__(self):
        printed_matrix = ''
        for i in range(len(self.matrix)):
            for j in self.matrix[i]:
                printed_matrix += f' {j} '
            printed_matrix += '\n'
        return printed_matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            row_len = len(self.matrix[0])
            for j in range(len(self.matrix)):
                if row_len != len(self.matrix[j]) or row_len != len(other.matrix[j]):
                    raise ValueError('Проверьте введённые данные, длина рядов должна быть одинаковой')
        else:
            raise ValueError('Матрицы разные, проверьте ввод')
        print('Начинаем складывать')
        result = []
        for i in range(len(self.matrix)):
            result_row = []
            row_sum = []
            for j in range(len(self.matrix[i])):
                row_sum.append(self.matrix[i][j] + other.matrix[i][j])
            result_row.append(row_sum)
            result.append(result_row)
        return result


# matrix = Matrix(
#     [
#         [
#             [1, 3, 4], [2, 8, 6], [7, 7, 1]
#         ],
#         [
#             [2, 8, 8], [3, 5, 2], [4, 1, 5]
#         ]
#     ])

matrix_a = Matrix(
    [
        [1, 3, 4], [2, 8, 6], [7, 7, 1]
    ]
)
print(matrix_a)
matrix_b = Matrix(
    [
        [2, 8, 8], [3, 5, 2], [4, 1, 5]
    ]
)
print(matrix_b)
get_matrix_sum = matrix_a + matrix_b
print(get_matrix_sum)
print('-------------------')

matrix_a = Matrix(
    [
        [1, 3], [2, 8], [7, 7]
    ]
)

matrix_b = Matrix(
    [
        [8, 8], [5, 2], [1, 5]
    ]
)

get_matrix_sum = matrix_a + matrix_b
print(get_matrix_sum)


matrix_a = Matrix(
    [
        [1, 3, 4, 5], [2, 8, 6, 1], [7, 7, 1]
    ]
)

matrix_b = Matrix(
    [
        [2, 8, 8], [3, 5, 2]
    ]
)

get_matrix_sum = matrix_a + matrix_b
print(get_matrix_sum)
