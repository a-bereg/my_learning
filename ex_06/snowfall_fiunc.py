import simple_draw as sd
from random import randint

_snowflakes_x = []
_snowflakes_y = []
_snowflakes_d = []
_snowflakes_s = []

sd.resolution = (1200, 600)


def snowflakes_create(quantity):
    global _snowflakes_x
    global _snowflakes_y
    global _snowflakes_d
    global _snowflakes_s

    for i in range(quantity):
        _snowflakes_x.append(randint(0, 1200))
        _snowflakes_y.append(randint(600, 1200))
        _snowflakes_d.append(randint(2, 11))
        _snowflakes_s.append(randint(5, 13))


def snowflakes_del():
    pass


def snowflakes_move():
    global _snowflakes_y
    for s in range(len(_snowflakes_y)):
        if _snowflakes_y[s] >= 0:
            _snowflakes_y[s] -= _snowflakes_s[s]


def snowflakes_color(snowflake_color=sd.COLOR_WHITE):
    sd.start_drawing()
    for i in range(len(_snowflakes_x)):
        snowflake_center = sd.get_point(_snowflakes_x[i], _snowflakes_y[i])
        sd.snowflake(center=snowflake_center, length=_snowflakes_d[i], color=snowflake_color)
    sd.finish_drawing()


def snowflakes_bottom_check():
    pass


# код для теста
snowflakes_create(50)
# print(len(_snowflakes_y), _snowflakes_y)
# print(len(_snowflakes_x), _snowflakes_x)
# print(len(_snowflakes_d), _snowflakes_d)
# snowflakes_move()
# print(len(_snowflakes_y), _snowflakes_y)

for i in range(680, 0, -1):
    snowflakes_color(snowflake_color=sd.background_color)
    snowflakes_move()
    snowflakes_color()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

