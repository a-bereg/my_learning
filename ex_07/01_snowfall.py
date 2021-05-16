# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.x_current_position = sd.random_number(20, 1180)
        self.y_current_position = sd.random_number(600, 1200)
        # self.x_previous_position = self.x_current_position
        # self.y_previous_position = self.y_current_position
        self.size = sd.random_number(2, 11)
        self.speed = sd.random_number(5, 13)

    def clear_previous_picture(self):
        point = sd.get_point(self.x_current_position, self.y_current_position)
        sd.start_drawing()
        sd.snowflake(center=point, length=self.size, color=sd.background_color)
        sd.finish_drawing()

    def move(self):
        # self.x_previous_position = self.x_current_position
        # self.y_previous_position = self.y_current_position
        self.x_current_position = self.x_current_position + (2 - sd.random_number(0, 4))
        self.y_current_position -= self.speed

    def draw(self):
        point = sd.get_point(self.x_current_position, self.y_current_position)
        sd.start_drawing()
        sd.snowflake(center=point, length=self.size)
        sd.finish_drawing()

    def can_fall(self):
        if self.y_current_position < self.size * 2:
            return False
        else:
            return True


# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
def get_flakes(count=5):
    flakes_list = []
    for i in range(count):
        flakes_list.append(Snowflake())
    return flakes_list


def get_fallen_flakes():
    count = 0
    for flake in flakes:
        if not flake.can_fall():
            count += 1
    return count


def append_flakes(count):
    for i in range(count):
        flakes.append(Snowflake())


flakes = get_flakes(count=5)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
