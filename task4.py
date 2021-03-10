your_dict = {}


def create_list(key_word, names):
    _names_list = []
    for name in names:
        if name[0] == key_word[0]:
            _names_list.append(name)
    return _names_list


def thesaurus(*args):
    result = {}
    for name in args:
        result.setdefault(name[0], create_list(name, args))
    return result


print(thesaurus('Иван', 'Илья', 'Мария', 'Пётр'))


def thesaurus_adv(*args):
    global your_dict
    for bio in args:
        name, surname = bio.split()
        if your_dict.get(surname[0]) == None:
            your_dict.setdefault(surname[0], thesaurus(bio))
        else:
            _ = your_dict.get(surname[0]) # этой строчкой получаю доступ к словарю внутреннему (по именам)
            bykeylist = _.setdefault(name[0], []) # получаю значение по ключу в этом словаре для того чтобы далее записывать туда новые значения
            bykeylist.append(bio) # запись значения
    return your_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Екатерина Сапирова"))


