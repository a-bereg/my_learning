# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def tr(start_p, corn, side_len):
    side1 = sd.get_vector(start_point=start_p, angle=corn, length=side_len)
    side1.draw()
    sd.circle(center_position=start_p, radius=5)

    side2 = sd.get_vector(start_point=side1.end_point, angle=side1.angle + 120, length=side_len)
    side2.draw()
    sd.circle(center_position=side1.end_point, radius=5)

    side3 = sd.get_vector(start_point=side2.end_point, angle=side2.angle + 120, length=side_len)
    side3.draw()
    sd.circle(center_position=side2.end_point, radius=5)


def fig_draw(start_p, corn, corn_num, side_len):
    ang = 360 / corn_num
    side = sd.get_vector(start_point=start_p, angle=corn, length=side_len)
    side.draw(color=[0, 255, 0])
    for i in range(1, corn_num):
        side = sd.get_vector(start_point=side.end_point, angle=side.angle + ang, length=side_len)
        side.draw()


st_point = sd.get_point(300, 300)
fig_draw(start_p=st_point, corn=0, corn_num=2, side_len=150)
st_point = sd.get_point(100, 20)
fig_draw(start_p=st_point, corn=60, corn_num=4, side_len=150)
st_point = sd.get_point(300, 20)
fig_draw(start_p=st_point, corn=20, corn_num=6, side_len=100)
st_point = sd.get_point(300, 400)
fig_draw(start_p=st_point, corn=90, corn_num=5, side_len=100)


#for angle in range(0, 361, 30):
#    tr(start_p=st_point, corn=angle, side_len=200)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
