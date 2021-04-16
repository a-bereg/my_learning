# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x_start = 50
x_end = 550
for i in range(7):
    start_point = sd.get_point(x_start, 50)
    end_point = sd.get_point(x_end, 550)
    sd.line(start_point, end_point, rainbow_colors[i], 5)
    x_start += 5
    x_end += 5

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

center = sd.get_point(-100, -600)
radius = 1000
line_width = 20

for i in range(7):
    sd.circle(center, radius, rainbow_colors[i], line_width)
    radius = radius + line_width +1

sd.pause()
