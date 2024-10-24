#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# есть список животных в зоопарке
def task_6():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
    zoo.insert(zoo.index('kangaroo'), 'bear')
    print("Список после добавления медведя:", zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
    zoo.extend(birds)
    print("Список после добавления птиц:", zoo)


# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
    zoo.remove('elephant')
    print("Список после удаления слона:", zoo)


# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
    lion_index = zoo.index('lion') + 1
    lark_index = zoo.index('lark') + 1

    print(f"Лев сидит в клетке номер {lion_index}")
    print(f"Жаворонок сидит в клетке номер {lark_index}")
