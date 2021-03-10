# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов, взятых
# из трёх списков (по одному слову из каждого списка):
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]

import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
sources = [nouns, adverbs, adjectives]


def get_joke(quant, repeats=0):
    """
    :param quant: аргумент отвечающий за количество шуток
    :param repeats: аргумент отвечающий за наличие повторов (флаг)
    :return: возвращает шутки
    """
    jokes = []
    if repeats != 0:
        for i in range(0, quant):
            for source in sources:
                word = random.choice(source)
                jokes.append(word)
                source.remove(word)
    else:
        for i in range(0, quant):
            for source in sources:
                word = random.choice(source)
                jokes.append(word)
    return jokes


print(get_joke(4, repeats=0))
print(get_joke(4, 1))
print(help(get_joke))


# не совсем понял вопроса про именнованные аргументы
# ведь имя аргументам мы даём в описании, если при вызове функции указывать их, то тоже да
# перменная repeats является флагом, который разрешает или запрещает повторы
