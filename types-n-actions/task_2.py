# Задание 2
# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента
# списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

letters_code = [number for number in range(1040, 1104)] # хранит символы юникод для букв верхнего и нижнего регистра


def check_number(pos):
    str = origin_list[pos]
    for i in range(0, len(str)):
        if ord(str[i]) in letters_code:
            print(f'{str} было пропущено')
            return 0
        else:
            print(f'{str} не было пропущено')
            if len(str) == 1:
                origin_list[pos] = '0' + origin_list[pos]
            elif origin_list[pos][0] == '+' and len(str) == 2: # потому что должен быть int, а я прошу символ
                origin_list[pos] = '+0' + origin_list[pos][1]
            elif origin_list[pos][0] == '-' and len(str) == 2:
                origin_list[pos] = '-0' + origin_list[pos][1]
            return 1


origin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

quotion_marks = []  # список, который будет хранить позиции чисел, перед и за которыми нужно вставить кавычки
for i in range(0, len(origin_list)):
    if check_number(i) == 1:
        quotion_marks.append(i)

origin_list_len = len(origin_list)  # переменная, созданая для хранения первоначальной длины массива
# используется для вычисления позиции, в которую необходимо вставить кавычку, тк при такой операции, постоянно меняется длина массива

for i in quotion_marks:
    if origin_list_len < len(origin_list):
        origin_list.insert(i + (len(origin_list) - origin_list_len), '"')
        origin_list.insert(i + 1 + (len(origin_list) - origin_list_len), '"')
    else:  # нужно для первых кавычек, тк после них меняется длина списка
        origin_list.insert(i, '"')  # вставляем кавычку перед числом
        origin_list.insert(i + 2, '"')  # перешагивая через элемент ставим вторую кавычку
print(origin_list)

# попробовать при проверке числа - сразу записывать его в строку с кавычками!!!!





###################### другой вариант решения ######################




def ifnumber_checking(element_of_list):
    if element_of_list.isdigit() == 1:
        print(f'{element_of_list} - число!')
        return twodigit_addition(element_of_list)
    elif element_of_list[0] == '+' or element_of_list[0] == '-' and element_of_list[1].isdigit() == 1:
        print(f'{element_of_list} тоже число')
        return twodigit_addition(element_of_list)
    return None


def twodigit_addition(number):
    if len(number) == 1:
        number = '0' + number
    elif len(number) == 2 and number[0] == '+':
        number = '+0' + number[1]
    elif len(number) == 2 and number[0] == '-':
        number = '-0' + number[1]
    return number


second_try_origin_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(second_try_origin_list):
    if ifnumber_checking(second_try_origin_list[i]) == None:
        i += 1
        continue
    second_try_origin_list[i] = ifnumber_checking(second_try_origin_list[i])
    second_try_origin_list.insert(i, '"')
    second_try_origin_list.insert(i + 2, '"')
    i += 2

print(second_try_origin_list)

result_str = ' '.join(second_try_origin_list)
print(result_str)
# сделал два решения, первое было через символы юникод, второе через функцию .isdigit()
# думаю, можно было бы сделать более изящно...