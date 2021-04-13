# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

x = []
y = []
d = []
s = []

# Заполняем случайными значениями стартовые параметры снежинок
for i in range(N):
    # Координаты (должны быть в пределах sd.resolution)
    x.append(sd.random_number(20, 1180))
    y.append(sd.random_number(600, 1200))
    # Размер
    d.append(sd.random_number(2, 11))
    # Скорость падения
    s.append(sd.random_number(5, 13))

while True:
    sd.start_drawing()
    for i in range(len(x)):
        if y[i] < d[i]:      # Если координата Y меньше размера снежинки, добавляем новую снежинку
            x[i] = sd.random_number(20, 1180)
            y[i] = sd.random_number(600, 700)
            d[i] = sd.random_number(2, 11)
            s[i] = sd.random_number(5, 13)
            continue
        point = sd.get_point(x[i], y[i])
        sd.snowflake(center=point, length=d[i], color=[0, 8, 98])    # Стираем снежинку (рисуем её цветом фона)
        y[i] -= s[i]
        fal = 2 - sd.random_number(0, 4)    # Случайное отклонение влево или вправо
        x[i] = x[i] + fal
        point = sd.get_point(x[i], y[i])
        sd.snowflake(center=point, length=d[i], color=[255, 255, 255])
    sd.finish_drawing()
    sd.sleep(0.05)
    if sd.user_want_exit():
        break
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


