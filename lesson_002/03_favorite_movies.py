#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# находим номера запятых
zap1 = my_favorite_movies.find(',')
zap2 = my_favorite_movies.find(',', zap1 + 2)
zap3 = my_favorite_movies.find(',', zap2 + 2)
zap4 = my_favorite_movies.find(',', zap3 + 2)

# Первый в списке
print(my_favorite_movies[0:my_favorite_movies.find(',')])
# последний
print(my_favorite_movies[zap4+2:])
# второй в списке
print(my_favorite_movies[zap1 + 2:zap2])
# Второй с конца
print(my_favorite_movies[zap3 + 2: zap4])
