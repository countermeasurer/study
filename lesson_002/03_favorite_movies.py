#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
film = {
    'terminator': 'Терминатор',
    'five': 'Пятый элемент',
    'avatar': 'Аватар',
    'other': 'Чужие',
    'back': 'Назад в будущее'
}

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
if film['terminator'] in my_favorite_movies:
    print(film['terminator'])

if film['back'] in my_favorite_movies:
    print(film['back'])

if film['five'] in my_favorite_movies:
    print(film['five'])

if film['other'] in my_favorite_movies:
    print(film['other'])

