# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 127, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (255, 0, 255)


def fig_draw(start_p, corn, corn_num, side_len):
    ang = 360 / corn_num
    side = sd.get_vector(start_point=start_p, angle=corn, length=side_len)
    side.draw(color=[0, 255, 0])
    for i in range(1, corn_num):
        side = sd.get_vector(start_point=side.end_point, angle=side.angle + ang, length=side_len)
        side.draw()


print('Возможные цвета:')
print('   0 : WHITE')
print('   1 : BLACK')
print('   2 : RED')
print('   3 : ORANGE')
print('   4 : YELLOW')
print('   5 : GREEN')
print('   6 : CYAN')
print('   7 : BLUE')
print('   8 : PURPLE')
color = input('Введите желаемый цвет:')

st_point = sd.get_point(300, 300)
fig_draw(start_p=st_point, corn=0, corn_num=2, side_len=150)
st_point = sd.get_point(100, 20)
fig_draw(start_p=st_point, corn=60, corn_num=4, side_len=150)
st_point = sd.get_point(300, 20)
fig_draw(start_p=st_point, corn=20, corn_num=6, side_len=100)
st_point = sd.get_point(300, 400)
fig_draw(start_p=st_point, corn=90, corn_num=5, side_len=100)

sd.pause()
