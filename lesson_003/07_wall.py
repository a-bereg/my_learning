# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
simple_draw.resolution = (1200, 600)
left_x, left_y = 0, -50
right_x, right_y = 100, 0

for y in range(12):
    if y % 2 == 0:
        left_x = 0
        right_x = 100
    else:
        left_x = -50
        right_x = 50
    left_y += 50
    right_y += 50
    for x in range(12):
        point_start = simple_draw.get_point(left_x, left_y)
        point_end = simple_draw.get_point(right_x, right_y)
        simple_draw.rectangle(point_start, point_end, (255, 255, 0), 1)
        left_x += 100
        right_x += 100

simple_draw.pause()
