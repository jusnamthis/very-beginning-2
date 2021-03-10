numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(number_name):
    print(numbers.get(number_name))
    # for key in numbers:
    #     if key == number_name:
    #         print(numbers[number_name])
    #         return
    # print('None')


num_translate('one')
num_translate('ten')
num_translate('zero')

# usr_input = input("Enter ur number")
# print(lambda num: numbers.get(usr_input))


#################### task 2 ##############################


def num_translate_adv(name):
    little_name = name.lower()
    if name == little_name:
        print(numbers.get(name))
    elif name[0].lower() == little_name[0] and name[1:] == little_name[1:]:
        print(numbers.get(name.lower()).capitalize())


num_translate_adv('Five')
num_translate_adv('five')
num_translate_adv('Eight')


# типом данных был выбран словарь для поиска значения по ключу
# словарь сделал глобальным скорее по интуиции и по вашим замечаниям из лекций
# внести его в условный main - дурной тон или технически менее правильно, или более правильно?