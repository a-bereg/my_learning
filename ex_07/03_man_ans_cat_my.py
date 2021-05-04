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
        self.cat = None

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
            self.money += 150
            self.fullness -= 20
        else:
            cprint('{} пошел на работу.' .format(self.name), color='magenta')
            self.house.money += 150
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

    def clean(self):
        cprint('{} убрался в доме.' .format(self.name), color='white')
        self.house.trash -= 100
        self.fullness -= 20

    def bay_cats_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота.'.format(self.name), color='blue')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('В доме мало денег - {}, кот останется голодным '.format(self.house.money), color='red')

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
        elif self.house.cat_food <= 30:
            self.bay_cats_food()
        elif self.house.trash >= 100:
            self.clean()
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

    def take_pet(self, cat):
        self.cat = cat
        self.cat.house = self.house
        cprint('{} завел кота {}'.format(self.name, self.cat.name))


class House:
    def __init__(self):
        self.food = 10
        self.money = 50
        self.trash = 0
        self.cat_food = 50

    def __str__(self):
        return 'В доме есть: еды - {}, денег - {}, Wiskas - {}, мусор - {}.' .format(
            self.food, self.money, self.cat_food, self.trash)


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def __str__(self):
        return 'Кот {}, сытость {}.' .format(self.name, self.fullness)

    def sleep(self):
        cprint('Кот {} спит.' .format(self.name), color='grey')
        self.fullness -= 10

    def eat(self):
        cprint('Кот {} поел.' .format(self.name), color='grey')
        self.house.cat_food -= 10
        self.fullness += 20

    def make_trash(self):
        cprint('Кот {} дерет обои.'.format(self.name), color='grey')
        self.house.trash += 5
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('Кот {} - умер' .format(self.name), color='red')
            return
        dice = randint(2, 3)
        if self.fullness <= 20:
            self.eat()
        elif dice == 2:
            self.sleep()
        elif dice == 3:
            self.make_trash()


sweet_home = House()
citizens = []
names_for_cit = ['Вася', 'Энди', 'Фёдор', 'Таня', 'Света', 'Миша', 'Алексей', 'Саша']
names_for_cat = ['Том', 'Гав', 'Мурзик', 'Бармалей', 'Мурка']
my_pet = Cat(names_for_cat[randint(0, 4)])         #создаем кота
my_pet2 = Cat(names_for_cat[randint(0, 4)])

# Создаем людей
for i in range(1):
    citizens.append(Man(names_for_cit[randint(0, 7)]))

# Заселяем людей в дом
for people in citizens:
    people.go_into_house(sweet_home)

citizens[0].take_pet(my_pet)
citizens[0].take_pet(my_pet2)

for day in range(1, 365):
    cprint('=================== День {} ===================' .format(day), color='yellow')
    for people in citizens:
        people.act()
    my_pet.act()
    my_pet2.act()
    print(sweet_home)
    cprint('-----------------------------------------------', color='yellow')
    for people in citizens:
        print(people)
    print(my_pet)
    print(my_pet2)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
