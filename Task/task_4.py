#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов
def task_4():
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код
    start = 0
    movies = []
    length = len(my_favorite_movies)
    for i in range(length):
        if my_favorite_movies[i] == ',' or i == length - 1:
            if i == length - 1:
                end = i + 1
            else:
                end = i
            movies.append(my_favorite_movies[start:end])
            start = i + 1

    print("Первый фильм: ", movies[0])
    print("Последний фильм:", movies[-1])
    print("Второй фильм:", movies[1])
    print("Второй с конца фильм:", movies[-2])