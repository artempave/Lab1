#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


def calculate_total_duration(songs, titles):
    total_duration = 0
    for song in songs:
        if isinstance(song, list) and song[0] in titles:
            total_duration += song[1]
        elif isinstance(songs, dict) and song in titles:
            total_duration += songs[song]
    return round(total_duration, 2)

# Расчет времени звучания для списка

def task_7():
    titles_list = ['Halo', 'Enjoy the Silence', 'Clean']
    total_time_list = calculate_total_duration(violator_songs_list, titles_list)
    print(f"Три песни звучат {total_time_list:.2f} минут")


# Есть словарь песен группы Depeche Mode

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код
    titles_dict = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    total_time_dict = calculate_total_duration(violator_songs_dict, titles_dict)
    print(f"А другие три песни звучат {total_time_dict:.2f} минут")
