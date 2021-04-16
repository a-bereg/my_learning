# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(x, y, color):
    """
    smile draw
    :param x: central point
    :param y: central point
    :param color: line color
    """
    center = sd.get_point(x, y)
    sd.circle(center, 50, color, 1)
    # eyes
    center = sd.get_point(x - 15, y + 10)
    sd.circle(center, 10, color, 1)
    sd.circle(center, 3, color, 1)
    center = sd.get_point(x + 15, y + 10)
    sd.circle(center, 10, color, 1)
    sd.circle(center, 3, color, 1)
    # mouth
    point1 = sd.get_point(x - 25, y - 15)
    point2 = sd.get_point(x - 10, y - 20)
    point3 = sd.get_point(x + 10, y - 20)
    point4 = sd.get_point(x + 25, y - 15)
    sd.lines((point1, point2, point3, point4), color)


for _ in range(5):
    cent = sd.random_point()
    clr = sd.random_color()
    smile(cent.x, cent.y, clr)

sd.pause()
