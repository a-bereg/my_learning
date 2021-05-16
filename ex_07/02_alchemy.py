# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return '{}' .format(self.name)

    def __add__(self, other):
        if isinstance(other, Air):
            new_obj = Storm()
            return new_obj
        elif isinstance(other, Fire):
            new_obj = Steam()
            return new_obj
        elif isinstance(other, Earth):
            new_obj = Mud()
            return new_obj
        else:
            return None


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return '{}' .format(self.name)

    def __add__(self, other):
        if isinstance(other, Water):
            new_obj = Storm()
            return new_obj
        elif isinstance(other, Fire):
            new_obj = Lightning()
            return new_obj
        if isinstance(other, Earth):
            new_obj = Dust()
            return new_obj
        else:
            return None


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return '{}' .format(self.name)

    def __add__(self, other):
        if isinstance(other, Water):
            new_obj = Steam()
            return new_obj
        elif isinstance(other, Air):
            new_obj = Lightning()
            return new_obj
        elif isinstance(other,Earth):
            new_obj = Lava()
            return new_obj
        else:
            return None


class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return '{}' .format(self.name)

    def __add__(self, other):
        if isinstance(other, Water):
            new_obj = Mud()
            return new_obj
        if isinstance(other, Air):
            new_obj = Dust()
            return new_obj
        if isinstance(other, Fire):
            new_obj = Lava()
            return new_obj
        else:
            return None


class Storm:
    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return 'Шторм' .format(self.name)


class Steam:
    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return '{}' .format(self.name)


class Mud:
    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return '{}' .format(self.name)


class Lightning:
    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return '{}' .format(self.name)


class Dust:
    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return '{}' .format(self.name)


class Lava:
    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return '{}' .format(self.name)


water = Water
air = Air
fire = Fire
print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
