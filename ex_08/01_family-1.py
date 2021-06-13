# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


########################################################
# Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self, name='home'):
        self.name = name
        self.money = 100
        self.food = 30
        self.mess = 0

    def __str__(self):
        return 'В доме {} денег, {} еды, {} беспорядка.'.format(self.money, self.food, self.mess)


class Husband:

    def __init__(self, name, house=None):
        self.name = name
        self.house = house
        self.happy = 100
        self.fullness = 30

    def __str__(self):
        return '{}: сытость - {}, счастье - {}.'.format(self.name, self.fullness, self.happy)
        # return super().__str__()

    def act(self):
        pass

    def eat(self):
        if self.house.food > 0:
            food = randint(10, 30)

            if self.house.food <= food:
                food = self.house.food

            self.house.food -= food
            self.fullness += food
            print('{} съел {} еды.'.format(self.name, food))
        else:
            print('{} Нечего кушать, в доме нет еды'.format(self.name))

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        print('{} сходил на работу.'.format(self.name))

    def gaming(self):
        self.fullness -= 10
        self.happy += 20
        print('{} поиграл в WoT!'.format(self.name))


class Wife:

    def __init__(self, name, house=None):
        self.name = name
        self.house = house
        self.happy = 100
        self.fullness = 30

    def __str__(self):
        return '{}: сытость - {}, счастье - {}.'.format(self.name, self.fullness, self.happy)
        # return super().__str__()

    def act(self):
        pass

    def eat(self):
        if self.house.food > 0:
            food = randint(10, 30)

            if self.house.food <= food:
                food = self.house.food

            self.house.food -= food
            self.fullness += food
            print('{} съел {} еды.'.format(self.name, food))
        else:
            print('{} Нечего кушать, в доме нет еды'.format(self.name))

    def shopping(self):
        if self.house.money > 0:
            products = randint(30, 50)
            if self.house.money <= products:
                products = self.house.money
            self.fullness -= 10
            self.house.money -= products
            self.house.food += products
            print('{} сходила в магазин, купила {} еды.'.format(self.name, products))
        else:
            print('В доме нет денег на продукты :(')

    def buy_fur_coat(self):
        self.fullness -= 10
        self.happy += 60
        self.house.money -= 350
        print('{} купила шубу :)'.format(self.name))

    def clean_house(self):
        self.fullness -= 10
        self.house.mess -= 100
        if self.house.mess < 0:
            self.house.mess = 0
        print('{} навела в доме порядок.'.format(self.name))


home = House('Sweet Home')
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

for day in range(1):
    cprint('================== День {} =================='.format(day), color='red')
    serge.work()
    masha.clean_house()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')

# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')
