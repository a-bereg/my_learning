# -*- coding: utf-8 -*-

import simple_draw as sd


def bubble(center, radius, color, width, step):
    """
    Рисуем пузырь, три вложенных оружности
    :param center: центр окружности
    :param radius: радиус
    :param color: цвет, кротеж (123, 123, 123), если не кортеж, то выбираем случайный цвет
    :param width: толщина линии
    :param step: расстояние между вложенными окружностями
    """
    if not isinstance(color, tuple):
        color = sd.random_color()

    for _ in range(3):
        sd.circle(center_position=center, radius=radius, color=color, width=width)
        radius = radius + step + width


sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
center = sd.get_point(50, 50)
radius = 40
for _ in range(3):
    sd.circle(center_position=center, radius=radius, color=(255, 255, 255), width=1)
    radius += 5

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
center = sd.get_point(350, 300)
bubble(center, 70, 0, 5, 10)

# Нарисовать 10 пузырьков в ряд
x = 200
radius = 60
for _ in range(10):
    center = sd.get_point(x, 500)
    x += 100
    bubble(center=center, radius=radius, color=(0, 255, 0), width=1, step=5)

# Нарисовать три ряда по 10 пузырьков
y = 100
radius = 40
for _ in range(3):
    x = 200
    y += 70
    for _ in range(10):
        center = sd.get_point(x, y)
        x += 100
        bubble(center=center, radius=radius, color=(255, 0, 0), width=1, step=5)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    center = sd.random_point()
    bubble(center=center, radius=40, color=0, width=1, step=4)

sd.pause()


