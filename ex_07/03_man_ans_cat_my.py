# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:
    def __init__(self, name):
        self.name = name
        self.money = 10
        self.fullness = 50
        self.food = 50
        self.house = None

    def __str__(self):
        return 'Я {}, сытость - {}, еды - {}, денег - {}.'.format(self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.house is None:
            if self.food >= 10:
                cprint('{} поел. :)' .format(self.name), color='yellow')
                self.fullness += 10
                self.food -= 10
            else:
                cprint('{} нет еды. :('.format(self.name), color='red')
        else:
            if self.house.food >= 10:
                cprint('{} поел. :)'.format(self.name), color='yellow')
                self.fullness += 10
                self.house.food -= 10
            else:
                cprint('{} нет еды. :('.format(self.name), color='red')

    def work(self):
        if self.house is None:
            cprint('{} пошел на работу.' .format(self.name), color='magenta')
            self.money += 50
            self.fullness -= 20
        else:
            cprint('{} пошел на работу.' .format(self.name), color='magenta')
            self.house.money += 50
            self.fullness -= 20

    def play_dota(self):
        cprint('{} играет в DOT-у. :)' .format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house is None:
            if self.money >= 50:
                cprint('{} сходил в магазин за едой.' .format(self.name), color='blue')
                self.money -= 50
                self.food += 50
            else:
                cprint('{} нет денег' .format(self.name), color='red')
        else:
            if self.house.money >= 50:
                cprint('{} сходил в магазин за едой.' .format(self.name), color='blue')
                self.house.money -= 50
                self.house.food += 50
            else:
                cprint('В доме мало денег - {} ' .format(self.house.money), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер!!!' .format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house is None and self.money <= 20:
            self.work()
        elif self.house is not None and self.house.money <= 20:
            self.work()
        elif self.house is None and self.food < 30:
            self.shopping()
        elif self.house is not None and self.house.food < 30:
            self.shopping()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_dota()

    def go_into_house(self, house):
        self.house = house
        self.fullness -= 10
        self.house.money += self.money
        self.money = 0
        self.house.food += self.food
        self.food = 0
        cprint('{} заселился в дом!!!' .format(self.name), color='cyan')


class House():
    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'В доме есть: еды - {}, денег - {}.' .format(self.food, self.money)


sweet_home = House()
vasya = Man(name='Вася')
vasya.go_into_house(house=sweet_home)

fedor = Man(name='Фёдор')
fedor.go_into_house(house=sweet_home)

for day in range(1, 360):
    cprint('=================== День {} ===================' .format(day), color='yellow')
    vasya.act()
    fedor.act()
    print(sweet_home)
    cprint('-----------------------------------------------', color='yellow')
    print(vasya)
    print(fedor)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
